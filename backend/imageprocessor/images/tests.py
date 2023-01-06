import pytest
from django.urls import reverse
from rest_framework import status
from images.models import Image

IMAGES_LIST = reverse('images-list')


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_working_endpoint(api_client):
    response = api_client.get(IMAGES_LIST)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_missing_id_image(api_client):
    response = api_client.get(IMAGES_LIST + '1/')
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_existing_id_image(api_client):
    Image.objects.create(title='Test', height=12, width=20)
    images = Image.objects.all()
    url = IMAGES_LIST + '1/'
    response = api_client.get(url)
    assert len(images) == 1
    assert response.status_code == status.HTTP_200_OK
