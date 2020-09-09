from .models import Product
from django.utils.translation import gettext_lazy as _


def hide_products(modeladmin, request, queryset):
    queryset.update(hidden=True)


hide_products.short_description = _("hide selected products").capitalize()


def show_products(modeladmin, request, queryset):
    queryset.update(hidden=False)


show_products.short_description = _("show selected products").capitalize()


def hide_all_products(modeladmin, request, queryset):
    for category in queryset:
        products = Product.objects.filter(category=category)
        products.update(hidden=True)


hide_all_products.short_description = _(
    "hide all products in selected categories").capitalize()


def show_all_products(modeladmin, request, queryset):
    for category in queryset:
        products = Product.objects.filter(category=category)
        products.update(hidden=False)


show_all_products.short_description = _(
    "show all products in selected categories").capitalize()
