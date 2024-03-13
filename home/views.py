from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
# from django.views.generic import ListView

# Create your views here.

#     return HttpResponse("Hello, welcome to home")
def index(request):
    return render(request, "home/homepage.html")

# class HomepageView(ListView):
#     model = Post
#     template_name = "homepage.html"


def index(request):
    home = Post.objects.get()
    template = loader.get_template('home/homepage.html')
    context = {
        'home' : home,
        }
    return HttpResponse(template.render(context, request))