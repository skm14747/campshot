from rest_framework import serializers, status
from users.models import User
from django.contrib.auth import authenticate
from .models import *


class UserSerializer(serializers.ModelSerializer):
    """
        User serializer for user CRUD API.
    """
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'name',
                  'mobile', 'about', 'avator', 'location')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PhotographerSerializer(serializers.ModelSerializer):

    # user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = PhotographerProfile
        fields = ('user', 'experience_in_months','genre')

    # def create(self, validated_data):

    #     photographer_profile = PhotographerProfile()
    #     photographer_profile.save()
    #     return photographer_profile
