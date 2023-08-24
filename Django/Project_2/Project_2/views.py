from django.http import HttpRequest
from django.shortcuts import render


def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "aboutus.html")

def contact(request):
    return render(request, "contact.html")

def loadUser(request):
    return render(request, "alta-usuario.html")

def loadEnterprise(request):
    return render(request, "alta-empresa.html")

def loadFile(request):
    return render(request, "alta-archivo.html")