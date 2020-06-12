<<<<<<< HEAD
rom django.urls import path, include

from electro import views


urlpatterns = [
    path('', views.index, name='home'),
]
=======
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> 7ee67a873ef8ac268ab1591a9ebe07c633fefe34
