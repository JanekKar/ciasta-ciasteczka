from .models import Product


def hide_products(modeladmin, request, queryset):
    queryset.update(hidden=True)


hide_products.short_description = "Hide selected products"


def show_products(modeladmin, request, queryset):
    queryset.update(hidden=False)


show_products.short_description = "Show selected products"


def hide_all_products(modeladmin, request, queryset):
    for category in queryset:
        products = Product.objects.filter(category=category)
        products.update(hidden=True)


hide_all_products.short_description = "Hide all products in selected categories"


def show_all_products(modeladmin, request, queryset):
    for category in queryset:
        products = Product.objects.filter(category=category)
        products.update(hidden=False)


show_all_products.short_description = "Show all products in selected categories"
