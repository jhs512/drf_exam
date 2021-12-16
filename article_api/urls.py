from django.urls import path

from article_api import views

urlpatterns = [
    path('', views.index),
]
