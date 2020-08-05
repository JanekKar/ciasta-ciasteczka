from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template_name = 'ciasta_ciasteczka/index.html'
    template = loader.get_template(template_name)
    context = {
        "": "",
    }
    return HttpResponse(template.render(context))


# Create your views here.
