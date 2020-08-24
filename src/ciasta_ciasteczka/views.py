from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone


def get_default_context():
    return {
        "year": timezone.now().year,
    }


def index(request):
    template_name = 'ciasta_ciasteczka/index.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    context.update(get_default_context())
    return HttpResponse(template.render(context))


def menu(request):
    template_name = 'ciasta_ciasteczka/index.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    return HttpResponse(template.render(context))


# Create your views here.
