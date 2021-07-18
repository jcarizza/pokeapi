from django.contrib import admin
from django.urls import path

from .views import PokemonView

urlpatterns = [
    path('pokemon/<int:pk>', PokemonView.as_view()),
]
