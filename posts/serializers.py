from rest_framework import serializers, status
from users.models import User
from django.contrib.auth import authenticate
from .models import *


class PostSerializer(serializers.ModelSerializer):
    """
        User serializer for user CRUD API.
    """
    class Meta:
        model = Post
        fields = ('user', 'is_private', 'post_picture')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('user', 'post', 'created')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'parent_comment', 'created')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('user', 'comment', 'parent_comment', 'created')
