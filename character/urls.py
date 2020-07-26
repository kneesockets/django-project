from django.urls import path
from character import views

app_name = 'character'

urlpatterns = [
    path('video/<slug:name>', views.video, name='video')
]
