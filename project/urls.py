from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from base import urls as base_urls
from character import urls as character_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls, namespace='base')),
    path('character/', include(character_urls, namespace='character'))
]

if settings.DEBUG:
    import debug_toolbar

    urlstoolbar = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += urlstoolbar
