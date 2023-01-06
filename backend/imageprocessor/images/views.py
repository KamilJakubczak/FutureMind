from rest_framework import viewsets, generics
from .models import Image
from .serializers import ImageSerializerCreate, ImageSerializerList
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ImagesList(viewsets.GenericViewSet, generics.ListCreateAPIView,
                 generics.RetrieveAPIView):

    queryset = Image.objects.all()
    serializer_class = ImageSerializerCreate

    def create(self, request, *args, **kwargs):
        self.serializer_class = ImageSerializerCreate
        return super().create(request, *args, **kwargs)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='title', description='Filter by title', required=False, type=str),
        ])
    def list(self, request, *args, **kwargs):
        if 'title' in request.query_params:
            search_str = request.query_params['title']
            self.queryset = Image.objects.filter(title__icontains=search_str)
        return super().list(request, args, kwargs)