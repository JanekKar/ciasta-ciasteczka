# Generated by Django 3.0.10 on 2020-09-15 16:58

import ciasta_ciasteczka.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciasta_ciasteczka', '0019_auto_20200908_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productphoto',
            options={'verbose_name': 'product photo', 'verbose_name_plural': 'product photos'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'product type', 'verbose_name_plural': 'product types'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'size', 'verbose_name_plural': 'sizes'},
        ),
        migrations.AlterModelOptions(
            name='sizeproductprice',
            options={'verbose_name': 'size and price of product', 'verbose_name_plural': 'sizes and prices of products'},
        ),
        migrations.AlterModelOptions(
            name='slideshowphoto',
            options={'verbose_name': 'slideshow photot', 'verbose_name_plural': 'slideshow photos'},
        ),
        migrations.AlterModelOptions(
            name='tray',
            options={'verbose_name': 'tray', 'verbose_name_plural': 'trays'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ciasta_ciasteczka.Category', verbose_name='parent category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='allergens',
            field=models.TextField(blank=True, null=True, verbose_name='allergens'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='ciasta_ciasteczka.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='hidden'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True, null=True, verbose_name='ingredients'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ciasta_ciasteczka.ProductType', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='alt_text',
            field=models.CharField(max_length=100, verbose_name='alternative text'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='main',
            field=models.BooleanField(default=False, verbose_name='main photo'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='photo',
            field=models.ImageField(upload_to=ciasta_ciasteczka.utils.RandomFileName('products/'), verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciasta_ciasteczka.Product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='price_unit',
            field=models.CharField(max_length=10, verbose_name='price unit'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='size',
            name='tray',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ciasta_ciasteczka.Tray', verbose_name='tray'),
        ),
        migrations.AlterField(
            model_name='size',
            name='weight',
            field=models.FloatField(blank=True, null=True, verbose_name='weight'),
        ),
        migrations.AlterField(
            model_name='sizeproductprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='sizeproductprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciasta_ciasteczka.Product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='sizeproductprice',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciasta_ciasteczka.Size', verbose_name='size'),
        ),
        migrations.AlterField(
            model_name='slideshowphoto',
            name='alt_text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='alternative text'),
        ),
        migrations.AlterField(
            model_name='slideshowphoto',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='hidden'),
        ),
        migrations.AlterField(
            model_name='slideshowphoto',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='tray',
            name='diameter',
            field=models.IntegerField(blank=True, null=True, verbose_name='diameter'),
        ),
        migrations.AlterField(
            model_name='tray',
            name='length',
            field=models.IntegerField(blank=True, null=True, verbose_name='length'),
        ),
        migrations.AlterField(
            model_name='tray',
            name='max_amount_of_people',
            field=models.IntegerField(default=0, verbose_name='maximum amount of people'),
        ),
        migrations.AlterField(
            model_name='tray',
            name='min_amount_of_people',
            field=models.IntegerField(default=0, verbose_name='minimum amount of people'),
        ),
        migrations.AlterField(
            model_name='tray',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tray',
            name='width',
            field=models.IntegerField(blank=True, null=True, verbose_name='width'),
        ),
    ]
