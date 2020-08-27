from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Tray(models.Model):
    name = models.CharField(max_length=50)
    diameter = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(blank=True, null=True)
    tray = models.ForeignKey(
        Tray, blank=True, null=True, on_delete=models.CASCADE)
    amount_of_people = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.TextField(blank=True, null=True)
    allergens = models.TextField(blank=True, null=True)
    hidden = models.BooleanField(default=False)

    size = models.ManyToManyField(Size)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def number_of_photos(self):
        return len(ProductPhoto.objects.filter(product=self,))
    number_of_photos.short_description = "Number of Photos"

    def get_main_pic_url(self):
        pictures = ProductPhoto.objects.get(product=self, main=True)
        if pictures:
            return pictures.photo.url


class ProductPhoto(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(
        Product, verbose_name="Product", on_delete=models.CASCADE)
    altr_text = models.CharField(max_length=100)
    photo = models.ImageField(
        height_field=None, width_field=None, max_length=None, upload_to='products/')
    main = models.BooleanField("Main photo", default=False)

    # TODO Validate only one image as main per product

    def __str__(self):
        return self.name


class SlideshowPhoto(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to='slideshow/', height_field=None, width_field=1024, max_length=None)
    altr_text = models.CharField(max_length=100, blank=True, null=True)
