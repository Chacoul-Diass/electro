from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def erreur (request):
    return render(request, 'pages/404.html')

def about (request):
    return render(request, 'pages/about.html')

def contact (request):

    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        sujet = request.POST['sujet']
        message = request.POST['message']
        
    else:
        return render(request, 'pages/contact-v1.html')


def faq (request):
    return render(request, 'pages/faq.html')

def store (request):
    return render(request, 'pages/store-directory.html')

def terms (request):
    return render(request, 'pages/terms-and-conditions.html')
