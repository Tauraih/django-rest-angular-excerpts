from django.urls import path

from . import views

app_name = 'progress'


urlpatterns = [
    path('index', views.index, name='index')
]
