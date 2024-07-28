from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('edit/<int:pk>/', views.tweet_edit, name='tweet_edit'),  
    path('delete/<int:pk>/', views.tweet_delete, name='tweet_delete'),  
    path('search/', views.tweet_search, name='tweet_search'),
]