from django.urls import path

from . import views

app_name = "aboutUs"

urlpatterns = [
    path("", views.index, name="about_us"),
]