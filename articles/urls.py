
from django.conf.urls import url
from django.urls import path

from .views import (
    welcome, 
    view_articles,
    search_article
    )

urlpatterns = [
    path('', welcome, name="welcome"),
    path('article', view_articles, name="articles"),
    path('search', search_article, name="search"),

    # url('^&')
]
