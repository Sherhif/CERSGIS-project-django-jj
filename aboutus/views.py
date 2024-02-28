from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, you are at the ABOUT US page")

def index(request):
    return render(request, "aboutus/about-us.html")