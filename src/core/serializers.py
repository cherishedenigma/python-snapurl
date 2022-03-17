from dataclasses import fields
from operator import mod
from rest_framework import serializers
from .models import SnapUrl, Post

class SnapUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapUrl
        fields = ('id','origin', 'hash','url')

class PostSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Post
            fields = ('origin',)