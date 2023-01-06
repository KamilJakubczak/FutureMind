from rest_framework import generics, viewsets
from .models import Image
from .serializers import ImageSerializer


class ImagesList(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer