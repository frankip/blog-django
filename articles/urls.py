from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from .views import (
    welcome, 
    create_article,
    view_articles,
    search_article,
    view_single_article,
    )

urlpatterns = [
    # path('', welcome, name="welcome"),
    path('', view_articles, name="articles"),
    path('new/article', create_article, name="new_articles"),
    path('article/<int:article_id>', view_single_article, name="single_article"),
    path('search', search_article, name="search"),

    # url('^&')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)