from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#     return HttpResponse("Hello, welcome to home")
def index(request):
    return render(request, "home/homepage.html")