from django.shortcuts import get_object_or_404
from django.shortcuts import render
from character.models import Video


def indice(request):
    videos = Video.objects.order_by('created_at').all()
    return render(request, 'character/indice.html', context={'videos': videos})


def video(request, name):
    video = get_object_or_404(Video, slug=name)
    return render(request, 'character/video.html', context={'video': video})
