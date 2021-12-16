from django.urls import path

from article_api import views

urlpatterns = [
    path('', views.ArticleList3.as_view()),
    path('<int:id>/', views.ArticleDetail3.as_view()),
]
