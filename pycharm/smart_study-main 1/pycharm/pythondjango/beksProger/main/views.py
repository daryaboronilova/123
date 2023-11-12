from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная Страница',

    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/explorer_base.html')

def auth(request):
    return render(request, 'main/auth.html')

def news(request):
    return render(request, 'main/news_home.html')
