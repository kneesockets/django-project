from django.urls import path, include
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='home')
]
