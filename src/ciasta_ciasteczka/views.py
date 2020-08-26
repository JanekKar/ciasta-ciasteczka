from django.shortcuts import render
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
    def get_products():
        cat = Category.objects.filter(slug=category_slug)
        return Product.objects.filter(category=cat)

    template_name = 'ciasta_ciasteczka/menu.html'
    template = loader.get_template(template_name)
    context = {
        'products': get_products(),
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
