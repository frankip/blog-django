from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)