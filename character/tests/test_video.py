from character.models import Video
from project.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy
import pytest


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def response(client, db, video):
    response = client.get(reverse('character:video', args=(video.slug,)))
    return response


@pytest.fixture
def response_not_found(client, db, video):
    response = client.get(reverse('character:video', args=(video.slug + '404',)))
    return response


def test_status_code_not_found(response_not_found):
    assert response_not_found.status_code == 404


def test_status_code(response):
    assert response.status_code == 200


def test_video_title(response, video):
    assert_contains(response, f'<h1 class="h2 my-3">{video.character}</h1>')


def test_video(response, video):
    assert_contains(response, f'src="https://www.youtube.com/embed/{video.youtube_id}"')
