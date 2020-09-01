from django.contrib import admin
from .models import *


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 3


class SizeProductPriceInline(admin.TabularInline):
    model = SizeProductPrice
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'hidden', 'number_of_photos')
    inlines = [ProductPhotoInline, SizeProductPriceInline]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Tray)
admin.site.register(ProductType)


# Register your models here.
