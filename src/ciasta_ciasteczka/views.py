from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import *

import random


def get_default_context():
    categories = {}
    parent_categories = Category.objects.filter(
        parent=None).order_by('priority')
    for parent in parent_categories:
        sub_categories = Category.objects.filter(
            parent=parent).order_by('name')
        active_sub_categories = []
        for sub_category in sub_categories:
            if sub_category.has_active_products():
                active_sub_categories.append(sub_category)
        if len(active_sub_categories) != 0:
            parent_name = parent.name
            parent.name = _('all...')
            active_sub_categories.append(parent)
            categories.update(
                {parent_name: active_sub_categories})

    return {
        "year": timezone.now().year,
        'categories': categories,
        'new_products': Product.objects.filter(hidden=False).order_by('-creation_date')[:4],
    }


def index(request):
    template_name = 'ciasta_ciasteczka/index.html'
    template = loader.get_template(template_name)
    context = {
        "slideshow_images": SlideshowPhoto.objects.filter(hidden=False),
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def category_details(request, category_slug):
    def get_products(category):
        all_products = []
        if category.is_parent():
            sub_categories = Category.objects.filter(parent=category)
            for sub_category in sub_categories:
                products = Product.objects.filter(
                    category=sub_category, hidden=False)
                all_products += products
            all_products = set(all_products)
        else:
            all_products = Product.objects.filter(
                category=category, hidden=False).order_by('modified')
        if len(all_products) == 0:
            raise Http404(_("Category does not exist"))
        else:
            return all_products

    def get_category():
        return get_object_or_404(Category, slug=category_slug)

    def get_random_background_image():
        images = SlideshowPhoto.objects.filter(hidden=False)
        if images:
            return random.choice(images)
        else:
            return None

    template_name = 'ciasta_ciasteczka/category_details.html'
    template = loader.get_template(template_name)
    category = get_category()
    context = {
        'category': category,
        'products': get_products(category),
        'background_image': get_random_background_image(),
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def product_details(request, product_id):
    template_name = 'ciasta_ciasteczka/product_details.html'
    template = loader.get_template(template_name)
    product = get_object_or_404(Product, id=product_id, hidden=False)
    context = {
        'product': product,
        'product_images': ProductPhoto.objects.filter(product_id=product_id).order_by('-main'),
        'sizes': SizeProductPrice.objects.filter(product_id=product_id).order_by('price'),
        'tort': product.product_type == ProductType.objects.get(name="Tort"),
        'accessories': Accessory.objects.filter(hidden=False),
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def cookies_info(request):
    template_name = 'ciasta_ciasteczka/cookies_info.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def handler400(request, exception):
    context = get_default_context()
    context.update({'error_400': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)


def handler403(request, exception):
    context = get_default_context()
    context.update({'error_403': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)


def handler404(request, exception):
    context = get_default_context()
    context.update({'error_404': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)


def handler500(request):
    context = get_default_context()
    context.update({'error_500': True,
                    'message': _("Sorry, something went wrong."),
                    'button_value': _('Come back to main page')})
    return render(request, 'error_page.html',
                  context=context)

# Create your views here.
