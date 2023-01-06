from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from images.views import ImagesList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'images', ImagesList, basename="images")


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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
