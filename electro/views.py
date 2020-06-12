from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'pages/home/index.html')

def erreur (request):
    return render(request, 'pages/home/404.html')

def about (request):
    return render(request, 'pages/home/about.html')

def contact (request):
    return render(request, 'pages/home/contact-v1.html')
