from django.contrib import admin
from .models import *
from .actions import *
from django.utils.translation import gettext_lazy as _


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    fields = ['alt_text', 'photo', 'main', 'image_tag']
    readonly_fields = ('image_tag',)
    extra = 3


class SizeProductPriceInline(admin.TabularInline):
    model = SizeProductPrice
    extra = 3


class SlideshowPhotoAdmin(admin.ModelAdmin):
    list_display = ['text', 'image_tag']
    readonly_fields = ('image_tag',)


class TrayAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_diameter',
                    'get_width', 'get_length', 'amount_of_people']

    def get_diameter(self, obj):
        if obj.diameter:
            return str(obj.diameter) + ' cm'
        else:
            return _("no data")
    get_diameter.short_description = _('diameter')

    def get_width(self, obj):
        if obj.width:
            return str(obj.width) + ' cm'
        else:
            return _("no data")
    get_width.short_description = _('width')

    def get_length(self, obj):
        if obj.length:
            return str(obj.length) + ' cm'
        else:
            return _("no data")
    get_length.short_description = _('length')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'allergen']
    actions = [mark_as_allergen, mark_as_notallergen]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'hidden', 'product_type',
                    'number_of_photos', 'number_of_categories']
    inlines = [ProductPhotoInline, SizeProductPriceInline]
    actions = [hide_products, show_products]
    list_filter = ['hidden', 'category', 'product_type__name']
    filter_horizontal = ('ingredients', 'category')
    search_fields = ['name']

    ordering = ['name']


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']
    actions = [hide_all_products, show_all_products]

    list_display = ['name', 'get_parent',
                    'has_active_products', 'number_of_active_products']

    def get_parent(self, obj):
        if obj.parent:
            return obj.parent
        else:
            return _("none").capitalize()
    get_parent.short_description = _("parent category")

    def number_of_active_products(self, obj):
        num = len(Product.objects.filter(category=obj))
        if num == 0:
            return _("none").capitalize()
        else:
            return num

    number_of_active_products.short_description = _(
        "number of active products")


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'hidden', 'get_price']
    actions = [hide_accessories, show_accessories]

    def get_price(self, obj):
        return str(obj.price) + "zł"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Tray, TrayAdmin)
admin.site.register(ProductType)
admin.site.register(SlideshowPhoto, SlideshowPhotoAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Accessory, AccessoryAdmin)


# Register your models here.
