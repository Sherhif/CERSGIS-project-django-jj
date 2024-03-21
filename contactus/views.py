from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactUs

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, CONTACT US.")

def index(request):
    return render(request, "contactus/contact-us.html")


# def ContactUs(request):
#     if request.method == "POST":
#         name= request.POST("name")
#         email= request.POST("email")
#         message= request.POST("message")
#         ContactUs= ContactUs.objects.create(name=name, email=email, messages=message)
#         messages.succes(reques, "data has been submitted")
#     return render(request, "/contact-us/")


# def ContactUs(request):
#     if request.method == "POST":
#         if request.POST.get("name") and request.POST.get("email") and request.POST.get("message"):
#             post=ContactUs()
#             post.name=request.POST.get("name")
#             post.email=request.POST.get("email")
#             post.message=request.POST.get("message")
#             post.save()

#             return render(request,"contactus/contact-us.html")



def process_ContactUs(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        user = ContactUs(name=name, email=email, message=message)
        user.save()

        return redirect('/contact-us/', message="message" )
    # else:
    #     return HttpResponse("Invalid input")