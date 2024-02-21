from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, here is BLOG.")

def index(request):
    return render(request, "blog/blog.html")