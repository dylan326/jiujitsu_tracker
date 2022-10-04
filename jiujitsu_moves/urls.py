from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('', views.index),
    path('add-move', views.addmove, name='add-move')
]
