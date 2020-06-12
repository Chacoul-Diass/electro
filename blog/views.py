from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'pages/blog/blog-v2.html')


def single_post(request):
    return render(request, 'pages/blog/single-blog-post.html')
