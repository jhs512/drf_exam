from django.urls import path

from article_api import views

urlpatterns = [
    path('', views.ArticleList2.as_view()),
    path('<int:id>/', views.ArticleDetail2.as_view()),
]
