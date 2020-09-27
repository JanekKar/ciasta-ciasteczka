from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)
