# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/edit/<int:tweet_id>/', views.tweet_edit, name='tweet_edit'),  
    path('tweets/delete/<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),  
    path('register/', views.register, name='register'), 


]

