from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import *

import random


def get_default_context(request):
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
        'new_products': Product.objects.all().order_by('-creation_date')[:4],
        'absolute_uri': request.build_absolute_uri
    }


def index(request):
    template_name = 'ciasta_ciasteczka/index.html'
    template = loader.get_template(template_name)
    context = {
        "slideshow_images": SlideshowPhoto.objects.filter(hidden=False),
        "": "",
    }
    context.update(get_default_context(request))
    return HttpResponse(template.render(context))


def category(request, category_slug):
    def get_products(category):
        all_products = []
        if category.is_parent():
            sub_categories = Category.objects.filter(parent=category)
            for sub_category in sub_categories:
                products = Product.objects.filter(category=sub_category)
                all_products += products
            all_products = set(all_products)
        else:
            all_products = Product.objects.filter(
                category=category, hidden=False)
        if len(all_products) == 0:
            raise Http404(_("Category does not exist"))
        else:
            return all_products

    def get_category():
        return get_object_or_404(Category, slug=category_slug)

    def get_random_background_image():
        images = SlideshowPhoto.objects.filter(hidden=False)
        return random.choice(images)
    template_name = 'ciasta_ciasteczka/menu.html'
    template = loader.get_template(template_name)
    category = get_category()
    context = {
        'category': category,
        'products': get_products(category),
        'background_image': get_random_background_image(),
        "": "",
    }
    context.update(get_default_context(request))
    return HttpResponse(template.render(context))


def product_details(request, product_id):
    template_name = 'ciasta_ciasteczka/product.html'
    template = loader.get_template(template_name)
    context = {
        'product': get_object_or_404(Product, id=product_id, hidden=False),
        'product_images': ProductPhoto.objects.filter(product_id=product_id).order_by('-main'),
        'sizes': SizeProductPrice.objects.filter(product_id=product_id).order_by('price'),
        "": "",
    }
    context.update(get_default_context(request))
    return HttpResponse(template.render(context))


def menu(request):
    template_name = 'ciasta_ciasteczka/menu.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    context.update(get_default_context(request))
    return HttpResponse(template.render(context))


def cookies(request):
    template_name = 'ciasta_ciasteczka/cookies.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    context.update(get_default_context(request))
    return HttpResponse(template.render(context))


def handler404_test(request):
    context = get_default_context(request)
    context.update({'error_500': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)


def handler400(request, exception):
    context = get_default_context(request)
    context.update({'error_400': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)


def handler403(request, exception):
    context = get_default_context(request)
    context.update({'error_403': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)


def handler404(request, exception):
    context = get_default_context(request)
    context.update({'error_404': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)


def handler500(request):
    context = get_default_context(request)
    context.update({'error_500': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)

# Create your views here.
