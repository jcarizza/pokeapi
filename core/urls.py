from django.urls import path

from .views import PokemonView

urlpatterns = [
    path("pokemon/<str:name>", PokemonView.as_view()),
]
