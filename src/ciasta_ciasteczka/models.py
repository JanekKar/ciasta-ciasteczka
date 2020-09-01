from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Tray(models.Model):
    name = models.CharField(max_length=50)
    diameter = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)

    # TODO validate if diameter or width/length are set (one or other)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(blank=True, null=True)
    tray = models.ForeignKey(
        Tray, blank=True, null=True, on_delete=models.CASCADE)
    min_amount_of_people = models.IntegerField(default=0)
    max_amount_of_people = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=50)
    price_unit = models.CharField(max_length=10)

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

    def __remove_polish_characters(self, word):
        pl_to_ang = {
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ź': 'z',
            'ż': 'z',
        }
        out = ""
        for letter in word:
            if letter in pl_to_ang:
                out += pl_to_ang[letter]
            else:
                out += letter
        return out

    def is_parent(self):
        return self.parent is None

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__remove_polish_characters(self.name))
        super(Category, self).save(*args, **kwargs)

    def has_active_products(self):
        if self.is_parent():
            sub_categories = Category.objects.filter(parent=self)
            for sub_category in sub_categories:
                if sub_category.has_active_products():
                    return True
            return False
        else:
            return Product.objects.filter(category=self, hidden=False).exists()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    ingredients = models.TextField(blank=True, null=True)
    allergens = models.TextField(blank=True, null=True)
    hidden = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)

    product_type = models.ForeignKey(
        ProductType, verbose_name="Type", on_delete=models.CASCADE, default=None, blank=False)

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

    def get_smallest_price(self):
        return SizeProductPrice.objects.filter(
            product=self).order_by('price')[0].price


class SizeProductPrice(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.size.name + "-" + self.product.name


class ProductPhoto(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(
        Product, verbose_name="Product", on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=100)
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
    alt_text = models.CharField(max_length=100, blank=True, null=True)
