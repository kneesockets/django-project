from project.django_assertions import assert_contains
from django.urls import reverse
from django.test import Client
import pytest

@pytest.fixture
def response(client):
    response = client.get(reverse('base:home'))
    return response

def test_home_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Home Page</title>')

def test_navbrand_link(response):
    assert_contains(response, f'href="{reverse("base:home")}"')