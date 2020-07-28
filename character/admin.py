from django.contrib import admin
from character import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('character', 'slug', 'created_at')
    ordering = ('created_at',)
    prepopulated_fields = {'slug': ('character',)}
