from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('', views.index),
    path('add-move', views.add_move, name='add-move')
]
