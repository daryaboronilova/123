from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('nachal', views.nachal, name='nachal'),
    path('registr', views.registr, name='registr'),
    path('news/<int:news_id>/', views.news, name='news')
]
