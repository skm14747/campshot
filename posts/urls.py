from django.conf.urls import url, include
from django.urls import path
from .views import PostView
from rest_framework import routers


urlpatterns = [
    path('posts/', PostView.as_view(), name='posts')
]
