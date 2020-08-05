from django.urls import path
from . import views

app_name = "ciasta_ciasteczka"

urlpatterns = [
    path('', views.index, name="index"),
]
