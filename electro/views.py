from django.shortcuts import render
from django.contrib.auth.models import User, auth
from electro.models import Info
# Create your views here.



def index(request):
    data = {
        'info':Info.objects.first(),
    }
    return render(request, 'pages/index.html', data)





def erreur (request):
    data = {
        'info':Info.objects.first(),
    }
    return render(request, 'pages/404.html', data)





def about (request):
    data = {
        'info':Info.objects.first(),
    }
    return render(request, 'pages/about.html',data)






def contact (request):
    data = {
        'info':Info.objects.first(),
    }

    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        sujet = request.POST['sujet']
        message = request.POST['message']
        
    else:
        return render(request, 'pages/contact-v1.html',data)





def faq (request):
    data = {
        'info':Info.objects.first(),
    }
    return render(request, 'pages/faq.html', data)





def store (request):
    data = {
        'info':Info.objects.first(),
    }
    return render(request, 'pages/store-directory.html',data)





def terms (request):
    data = {
        'info':Info.objects.first(),
    }
    return render(request, 'pages/terms-and-conditions.html',data)
