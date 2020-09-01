from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "ciasta_ciasteczka"

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('category/<str:category_slug>', views.category, name="category"),
    path('product/<int:product_id>', views.product_details, name="product_details"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
