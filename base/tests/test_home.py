from project.django_assertions import assert_contains
from django.test import Client


def test_home_status_code(client: Client):
    response = client.get('/')
    assert response.status_code == 200


def test_title(client: Client):
    response = client.get('/')
    assert_contains(response, '<title>Home Page</title>')
