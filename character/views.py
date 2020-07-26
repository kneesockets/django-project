from django.shortcuts import render


def video(request, name):
    return render(request, 'character/video.html')
