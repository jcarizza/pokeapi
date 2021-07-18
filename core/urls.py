from django.contrib import admin
from django.urls import path

from .views import PokemonView

urlpatterns = [
    path('pokemon/<int:id>', PokemonView.as_view()),
]
