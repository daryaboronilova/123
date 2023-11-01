from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('schedule', views.schedule, name='schedule'),
    path('nachal', views.nachal, name='nachal'),
    path('registr', views.registr, name='registr'),
    path('news/<int:news_id>/', views.news, name='news'),
    path('chat', views.chat, name='chat'),
    path('contacts', views.contacts, name='contacts'),
    path('profile', views.profile, name='profile')
]
