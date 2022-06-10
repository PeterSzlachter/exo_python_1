from django.contrib import admin
from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article-01"),
    # path('article-02/', article_02, name="blog-article-02"),
    # path('article-03/', article_03, name="blog-article-03")
]
