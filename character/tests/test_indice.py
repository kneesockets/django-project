from character.models import Video
from project.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy
import pytest


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def response(client, videos):
    return client.get(reverse('character:indice'))


def test_status_code(response):
    assert response.status_code == 200


def test_title(response, videos):
    for video in videos:
        assert_contains(response, video.character)


def test_link(response, videos):
    for video in videos:
        assert_contains(response, f'href="{reverse("character:video", args=(video.slug,))}"')
