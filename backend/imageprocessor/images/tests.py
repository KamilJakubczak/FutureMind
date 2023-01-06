import pytest
from django.urls import reverse
from rest_framework import status
from images.models import Image
from utils import generate_dummy_image


IMAGES_LIST = reverse('images-list')


def create_image_in_db(api_client, title='title'):
    name = 'test'
    extension = 'jpeg'
    full_name = f'{name}.{extension}'
    image = generate_dummy_image(filename=name, extension=extension)
    payload = {'title': title, 'width': 2, 'height': 2,
               'image': (full_name, image, 'image/jpeg')}

    response = api_client.post(IMAGES_LIST, data=payload)
    return response


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


# API
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
    create_image_in_db(api_client)
    images = Image.objects.all()
    url = IMAGES_LIST + '1/'
    response = api_client.get(url)
    assert len(images) == 1
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_filtering(api_client):

    create_image_in_db(api_client, title='test')
    create_image_in_db(api_client)
    images = Image.objects.all()
    response = api_client.get(IMAGES_LIST, {'title': 'tl'})
    assert len(images) == 2
    assert response.data['count'] == 1


@pytest.mark.django_db
def test_creating_image_ok(api_client):
    response = create_image_in_db(api_client)
    assert response.status_code == status.HTTP_201_CREATED
