from django.shortcuts import render

from blog import models
from django.http import  HttpResponse
# Create your views here.

def index(request):
    data = {
        'categories': models.BlogCategory.objects.all(),
        'articles': models.Article.objects.order_by('date_pub'),
    }
    return render(request, 'pages/blog/blog-v2.html', data)


def single_post(request, var):
    return render(request, 'pages/blog/single-blog-post.html')
    # return HttpResponse(request, var)
