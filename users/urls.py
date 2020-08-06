from django.conf.urls import url, include
from django.urls import path
from .views import UserViewSet, HomeView, PhotographerView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('home/', HomeView.as_view(), name='hello'),
    path('photographer/', PhotographerView.as_view(), name='photographer')
]
