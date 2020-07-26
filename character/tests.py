from project.django_assertions import assert_contains
from django.urls import reverse
import pytest


@pytest.fixture
def response(client):
    response = client.get(reverse('character:video', args=('yoshida-yuuko',)))
    return response


def test_status_code(response):
    assert response.status_code == 200


def test_video_title(response):
    assert_contains(response, '<h1 class="h2 my-3">Yoshida Yuko</h1>')


def test_video(response):
    assert_contains(response, 'src="https://www.youtube.com/embed/pn1Eqqc2XoQ"')
