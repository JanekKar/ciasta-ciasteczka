from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone

from .models import *


def get_default_context():
    categories = {}
    parent_categories = Category.objects.filter(parent=None)
    for parent in parent_categories:
        sub_categories = Category.objects.filter(parent=parent)
        active_sub_categories = []
        for sub_category in sub_categories:
            if sub_category.has_active_products():
                active_sub_categories.append(sub_category)
        if len(active_sub_categories) != 0:
            categories.update(
                {parent.name: active_sub_categories})

    return {
        "year": timezone.now().year,
        'categories': categories,
    }


def index(request):
    template_name = 'ciasta_ciasteczka/index.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def category(request, category_slug):
    def get_products(category):
        if category.is_parent():
            sub_categories = Category.objects.filter(parent=category)
            all_products = []
            for sub_category in sub_categories:
                products = Product.objects.filter(category=sub_category)
                all_products += products
            return set(all_products)
        else:
            return Product.objects.filter(category=category, hidden=False)

    def get_category():
        return get_object_or_404(Category, slug=category_slug)

    template_name = 'ciasta_ciasteczka/menu.html'
    template = loader.get_template(template_name)
    category = get_category()
    context = {
        'category': category,
        'products': get_products(category),
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def product_details(request, product_id):
    template_name = 'ciasta_ciasteczka/product.html'
    template = loader.get_template(template_name)
    context = {
        'product': get_object_or_404(Product, id=product_id, hidden=False),
        'product_images': ProductPhoto.objects.filter(product_id=product_id),
        'sizes': SizeProductPrice.objects.filter(product_id=product_id),
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def menu(request):
    template_name = 'ciasta_ciasteczka/menu.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


# Create your views here.
