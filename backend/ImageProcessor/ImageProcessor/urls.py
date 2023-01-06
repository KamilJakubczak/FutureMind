from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Images.views import ImagesList


router = DefaultRouter()
router.register(r'images', ImagesList, basename="image")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
