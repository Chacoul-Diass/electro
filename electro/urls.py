from django.urls import path, include

from electro import views


urlpatterns = [
    path('', views.index, name='home'),
]
