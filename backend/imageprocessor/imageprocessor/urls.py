from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from images.views import ImagesList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'images', ImagesList, basename="images")

#TODO Add swagger

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
# OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
