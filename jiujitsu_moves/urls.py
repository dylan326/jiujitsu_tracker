from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('', views.index),
    path('add-move', views.add_move, name='add-move'),
    path('search-moves', views.search_moves, name="search-moves"),
    path('half-guard-moves', views.half_guard_moves, name="half-guard-moves"),
]
