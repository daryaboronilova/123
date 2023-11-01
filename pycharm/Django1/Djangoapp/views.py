from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    return render(request, 'Djangoapp/index.html')


def about(request):
    return render(request, 'Djangoapp/about.html')


def news(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request, 'Djangoapp/news.html', {'news_object': news})


def contacts(request):
    return render(request, 'Djangoapp/contacts.html')


def nachal(request):
    news = News.objects.all()
    return render(request, 'Djangoapp/nachal.html', {'news': news})


def registr(request):
    return render(request, 'Djangoapp/registr.html')

