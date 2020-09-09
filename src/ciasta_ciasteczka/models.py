from django.dispatch import receiver
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from . import utils

import os
from PIL import Image


class Tray(models.Model):

    class Meta:
        verbose_name = _("tray")
        verbose_name_plural = _("trays")

    name = models.CharField(verbose_name=_("name"), max_length=50)
    diameter = models.IntegerField(
        verbose_name=_("diameter"), blank=True, null=True)
    width = models.IntegerField(verbose_name=_("width"), blank=True, null=True)
    length = models.IntegerField(
        verbose_name=_("length"), blank=True, null=True)
    min_amount_of_people = models.IntegerField(
        verbose_name=_("minimum amount of people"), default=0)
    max_amount_of_people = models.IntegerField(
        verbose_name=_("maximum amount of people"), default=0)

    # TODO validate if diameter or width/length are set (one or other)

    def __str__(self):
        return self.name


class Size(models.Model):

    class Meta:
        verbose_name = _("size")
        verbose_name_plural = _("sizes")

    name = models.CharField(verbose_name=_("name"), max_length=50)
    weight = models.FloatField(verbose_name=_("weight"), blank=True, null=True)
    tray = models.ForeignKey(Tray, verbose_name=_(
        "tray"), blank=False, null=True, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class ProductType(models.Model):

    class Meta:
        verbose_name = _("product type")
        verbose_name_plural = _("product types")

    name = models.CharField(verbose_name=_("name"), max_length=50)
    price_unit = models.CharField(verbose_name=_("price unit"), max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    name = models.CharField(verbose_name=_("name"), unique=True, max_length=50)
    description = models.TextField(verbose_name=_(
        "description"), blank=True, null=True)
    parent = models.ForeignKey("Category", verbose_name=_(
        "category"), on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(verbose_name=_("slug"), unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(utils.convert_to_ASCI_characters(self.name))
        super(Category, self).save(*args, **kwargs)

    def is_parent(self):
        return self.parent is None

    def has_active_products(self):
        if self.is_parent():
            sub_categories = Category.objects.filter(parent=self)
            for sub_category in sub_categories:
                if sub_category.has_active_products():
                    return True
            return False
        else:
            return Product.objects.filter(category=self, hidden=False).exists()


class Product(models.Model):

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    name = models.CharField(verbose_name=_("name"), max_length=60)
    description = models.TextField(verbose_name=_("description"),)
    ingredients = models.TextField(verbose_name=_(
        "ingredients"), blank=True, null=True)
    allergens = models.TextField(verbose_name=_(
        "allergens"), blank=True, null=True)
    hidden = models.BooleanField(verbose_name=_("hidden"), default=False)
    creation_date = models.DateTimeField(
        verbose_name=_("creation date"), auto_now_add=True)
    product_type = models.ForeignKey(ProductType, verbose_name=_(
        "type"), on_delete=models.CASCADE, default=None, blank=False)
    category = models.ManyToManyField(Category, verbose_name=_("category"),)

    def __str__(self):
        return self.name

    def number_of_photos(self):
        return len(ProductPhoto.objects.filter(product=self,))
    number_of_photos.short_description = _("number of photos").capitalize()

    def number_of_categories(self):
        return len(Category.objects.filter(product=self,))
    number_of_categories.short_description = _(
        "number of categories").capitalize()

    def get_main_pic(self):
        picture = ProductPhoto.objects.get(product=self, main=True)
        if picture:
            return picture
        else:
            return None

    def get_smallest_price(self):
        return SizeProductPrice.objects.filter(
            product=self).order_by('price')[0].price


class SizeProductPrice(models.Model):

    class Meta:
        verbose_name = _("size and price of product")
        verbose_name_plural = _("sizes and prices of products")

    size = models.ForeignKey(Size, verbose_name=_(
        "size"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_(
        "product"), on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_(
        "price"), max_digits=5, decimal_places=2)

    def __str__(self):
        return self.size.name + "-" + self.product.name


class ProductPhoto(models.Model):

    class Meta:
        verbose_name = _("product photo")
        verbose_name_plural = _("product photos")

    product = models.ForeignKey(Product, verbose_name=_(
        "product"), on_delete=models.CASCADE)
    alt_text = models.CharField(verbose_name=_(
        "alternative text"), max_length=100)
    photo = models.ImageField(verbose_name=_("image"), upload_to=utils.RandomFileName(
        'products/'), height_field=None, width_field=None, max_length=None)
    main = models.BooleanField(verbose_name=_("main photo"), default=False)

    def save(self, *args, **kwargs):
        if self.main:
            temp = ProductPhoto.objects.filter(product=self.product, main=True)
            if temp:
                temp.update(main=False)
        super(ProductPhoto, self).save(*args, **kwargs)

    def __str__(self):
        return self.alt_text


@receiver(models.signals.post_delete, sender=ProductPhoto)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=ProductPhoto)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = ProductPhoto.objects.get(pk=instance.pk).photo
    except ProductPhoto.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class SlideshowPhoto(models.Model):

    class Meta:
        verbose_name = _("slideshow photot")
        verbose_name_plural = _("slideshow photos")

    text = models.CharField(verbose_name=_(
        "text"), max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=utils.RandomFileName('slideshow/'))
    alt_text = models.CharField(verbose_name=_(
        "alternative text"), max_length=100, blank=True, null=True)
    hidden = models.BooleanField(verbose_name=_("hidden"), default=False)

    def save(self, *args, **kwargs):
        super(SlideshowPhoto, self).save(*args, **kwargs)
        imag = Image.open(self.image.path)
        if imag.width > 1024:
            output_size = (1024, 1024)
            imag.thumbnail(output_size)
            imag.save(self.image.path)

    def __str__(self):
        return self.text
