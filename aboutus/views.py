from django.shortcuts import render
from .models import AboutUs
from django.template import loader

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse



# def index(request):
#     return HttpResponse("Hello, you are at the ABOUT US page")

def index(request):
    return render(request, "about-us.html")

# def AboutUs (request):
#     aboutus = AboutUs.title.object.all().values()
#     template = loader.get_template("aboutus/about-us.html")
#     context = {
#         'AboutUs' : "aboutus",
#     }
#     return HttpResponse(template.render(context, request))


# def aboutus(request, id):
#     aboutus = AboutUs.title.get(id=id)
#     template = loader.get_template('aboutus.html')
#     context = {
#         'aboutus' : aboutus
#     }
#     return HttpResponse(template.render(context, request))



def index(request):
    aboutus = AboutUs.objects.get()
    template = loader.get_template('aboutus/about-us.html')
    context = {
        'aboutus' : aboutus,
        }
    return HttpResponse(template.render(context, request))

# def index(request):
#     context = {'aboutus' : {'AboutUs'} }
#     return render(request, "aboutus/about-us.html", context)