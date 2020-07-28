
from django.conf.urls import url
from django.urls import path

from .views import welcome

urlpatterns = [
    path('', welcome, name="welcome")
    # url('^&')
]
