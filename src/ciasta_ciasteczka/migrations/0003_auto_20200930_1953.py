# Generated by Django 3.0.10 on 2020-09-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciasta_ciasteczka', '0002_accessory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessory',
            options={'ordering': ['name'], 'verbose_name': 'accessory', 'verbose_name_plural': 'accessories'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name'], 'verbose_name': 'ingredient', 'verbose_name_plural': 'ingredients'},
        ),
        migrations.AddField(
            model_name='product',
            name='priority',
            field=models.DecimalField(decimal_places=0, default=5, max_digits=1, verbose_name='priority'),
        ),
    ]
