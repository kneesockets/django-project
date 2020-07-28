from django.db import models


class Video(models.Model):
    character = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    youtube_id = models.CharField(max_length=24)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Character: {self.character}'
