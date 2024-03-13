from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPage

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, here is BLOG.")

def index(request):
    return render(request, "blog/blog.html")

def index(request):
    blog = BlogPage.objects.get()
    template = loader.get_template('blog/blog.html')
    context = {
        'blog' : blog,
        }
    return HttpResponse(template.render(context, request))