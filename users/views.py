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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class HomeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'message': 'Hello ' + request.user.name
        }
        return Response(content)


class PhotographerView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PhotographerSerializer

    def get(self, request):

        print(request.data)
        return Response(request.data)

    def post(self, request):

        print(request.data['experience_in_months'])
        pp = PhotographerProfile(
            user=request.user, experience_in_months=int(request.data['experience_in_months']))

        pp.save()

        pps = PhotographerSerializer(pp)

        return Response(pps.data)
