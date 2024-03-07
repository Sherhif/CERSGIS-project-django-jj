from django.urls import path

from . import views

from .views import AboutUs

app_name = "aboutUs"

urlpatterns = [
    path("", views.index, name="about_us"),
    # path('aboutus/about-us.html', name='aboutus_aboutus')
]