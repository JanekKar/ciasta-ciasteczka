# Generated by Django 3.0.9 on 2020-08-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciasta_ciasteczka', '0007_auto_20200827_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideshowPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='slideshow/', width_field=1024)),
                ('altr_text', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
