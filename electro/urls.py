from django.urls import path, include
from electro import views


urlpatterns = [
    path('', views.index, name='home'),
    path('erreur', views.erreur, name='erreur'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('store', views.store, name='store'),
    path('terms', views.terms, name='terms'),
]
