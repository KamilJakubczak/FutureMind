from rest_framework import serializers
from .models import Image


class ImageSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'width', 'height', 'image']


class ImageSerializerList(serializers.ModelSerializer):
    url = serializers.ImageField(source='image')

    class Meta:
        model = Image
        fields = ['id', 'url', 'title', 'width', 'height']
