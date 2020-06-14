from django.shortcuts import render
import datetime
# from django.utils import timezone
from blog import models
from django.http import  HttpResponse
# Create your views here.

def index(request):
    date = datetime.date.today()
    # start_week = date - datetime.timedelta(date.weekday())
    # end_week = start_week + datetime.timedelta(7)
    data = {
        'categories': models.BlogCategory.objects.all(),
        'articles': models.Article.objects.order_by('date_pub'),
        'recents': models.Article.objects.filter(date_pub__gte=date),
    }
    return render(request, 'pages/blog/blog-v2.html', data)


def single_post(request, id):
    date = datetime.date.today()
    data = {
        'article': models.Article.objects.get(id=id),
        'recents': models.Article.objects.filter(date_pub__gte=date),
        'comment': models.Commentaire.objects.filter(article_id=id).filter(status=True)
    }
    return render(request, 'pages/blog/single-blog-post.html', data)
    # return HttpResponse(request, var)
