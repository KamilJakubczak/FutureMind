from rest_framework import viewsets, generics
from .models import Image
from .serializers import ImageSerializerCreate, ImageSerializerList


class ImagesList(viewsets.GenericViewSet, generics.ListCreateAPIView,
                 generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializerList

    def create(self, request, *args, **kwargs):
        serializer_class = ImageSerializerList
