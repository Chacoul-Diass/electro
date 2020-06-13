from django.urls import path, include
from blog import views


urlpatterns = [
    path('blog', views.index, name='blog'),
    path('blog/article/<str:var>/', views.single_post, name='article'),

]
