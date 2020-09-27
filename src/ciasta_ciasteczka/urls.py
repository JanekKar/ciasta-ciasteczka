from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from .models import Product, Category
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from .sitemaps import StaticViewSitemap


app_name = "ciasta_ciasteczka"

sitemaps = {
    'category': GenericSitemap({
        'queryset': Category.objects.filter(),
    }, priority=0.9),
    'manu': GenericSitemap({
        'queryset': Product.objects.filter(hidden=False),
        'date_field': 'modified',
    }, priority=0.5),
    # 'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name="index"),

    path('kategorie/<str:category_slug>',
         views.category_details, name="category_details"),

    path('produkt/<int:product_id>', views.product_details, name="product_details"),

    path('ciasteczka/', views.cookies_info, name="cookies_info"),

    path("robots.txt", TemplateView.as_view(
        template_name="ciasta_ciasteczka/robots.txt", content_type="text/plain")),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
