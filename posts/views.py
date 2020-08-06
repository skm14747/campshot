from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .models import User

# Create your views here.


class PostView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            posts = request.user.post_set.all()

            posts = PostSerializer(posts)
        except Exception as e:
            raise Exception('Exception occured @ post view' + e)

        return Response(posts.data)
