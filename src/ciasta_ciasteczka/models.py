from django.db import models

class Tray(models.Model):
    name = models.CharField(max_length=50)
    diameter = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()

class Size(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(null = True)
    tray = models.ForeignKey(Tray, null = True,on_delete=models.CASCADE)
    amount_of_people = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    description =models.TextField(null=True)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.TextField(null=True)
    allergens = models.TextField(null=True)
    hidden = models.BooleanField(default=False)

    size = models.ManyToManyField(Size)
    category = models.ManyToManyField(Category)

class ProductPhoto(models.Model):
    product = models.OneToOneField(Product, verbose_name="Product", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    altr_text = models.CharField(max_length=100)
    photo = models.ImageField(height_field=None, width_field=None, max_length=None)


# Create your models here.
