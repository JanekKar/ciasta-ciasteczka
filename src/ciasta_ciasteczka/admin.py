from django.contrib import admin
from .models import *
from .actions import *


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 3


class SizeProductPriceInline(admin.TabularInline):
    model = SizeProductPrice
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'hidden', 'product_type',
                    'number_of_photos', 'number_of_categories')
    inlines = [ProductPhotoInline, SizeProductPriceInline]
    actions = [hide_products, show_products]
    list_filter = ['hidden', 'product_type', 'category']


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']
    actions = [hide_all_products, show_all_products]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Tray)
admin.site.register(ProductType)
admin.site.register(SlideshowPhoto)


# Register your models here.
