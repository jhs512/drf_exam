from django.urls import path

from article_api import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('<int:id>/', views.ArticleDetail.as_view()),
]
