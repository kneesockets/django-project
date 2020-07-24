from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from base import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls, namespace='base'))
]

if settings.DEBUG:
    import debug_toolbar

    urlstoolbar = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += urlstoolbar
