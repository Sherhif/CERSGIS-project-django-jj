from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def roles(request):
    return HttpResponse("Hello, welcome to the roles.")


def institutions(request):
    return HttpResponse("Hello, welcome to the institutions.")

def permisions(request):
    return HttpResponse("Hello, welcome to the PERMISSIONS.")

def sectors(request):
    return HttpResponse("Hello, welcome to the SECTORS.")

def teams(request):
    return HttpResponse("Hello, welcome to the TEAMS.")

def policy(request):
    return HttpResponse("Hello, welcome to the POLICY.")