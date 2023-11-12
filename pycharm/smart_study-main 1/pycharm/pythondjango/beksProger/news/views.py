from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
# Create your views here.

def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news':news})

class NewsDetaiview(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

def create (request):
    form = ArticlesForm()

    data = {
        'form': form
    }
    return render(request, 'news/create.html',data)