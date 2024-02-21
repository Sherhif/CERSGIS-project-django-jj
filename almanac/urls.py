"""
URL configuration for almanac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from contactus import views
from dashboard import views as dashboardviews

extra_patterns = [
    path("institutions/", dashboardviews.institutions),
    path("roles/", dashboardviews.roles),
    path("permisions/", dashboardviews.permisions),
    path("sectors/", dashboardviews.sectors),
    path("teams/", dashboardviews.teams),
    path("policy/", dashboardviews.policy),
]



urlpatterns = [
   path("", include("home.urls")),
   path("policies/", include("policies.urls")),
   path("legislations/", include("legislations.urls")),
   path("dashboard/", include(extra_patterns)),
   path("community-engagement/", include("communityengagement.urls")),
   path("contact-us/", views.index, name="contactus.urls"),
   path("blog/", include("blog.urls")),
   path("about-us/", include ("aboutus.urls")),
   path('admin/', admin.site.urls),
]



