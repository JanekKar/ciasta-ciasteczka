from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone

from .models import *


def get_default_context():
    categories = {}
    parent_categories = Category.objects.filter(parent=None)
    for parent in parent_categories:
        categories.update(
            {parent.name: Category.objects.filter(parent=parent)})

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


def menu(request):
    template_name = 'ciasta_ciasteczka/menu.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


# Create your views here.
