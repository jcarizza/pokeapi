import pytest

from rest_framework.test import APIRequestFactory

from factories import PokemonFactory, EvolutionFactory
from core.views import PokemonView


@pytest.fixture
def pokemon():
    return PokemonFactory.create()


class TestPokemonResource:


    def test_get_pokemon(self, db, pokemon):
        factory = APIRequestFactory()
        request = factory.get('/pokemon/{pokemon.name}')
        view = PokemonView.as_view()
        response = view(request, name=pokemon.name)

        assert response.status_code == 200
        assert response.data['name'] == pokemon.name
        assert response.data['id'] == pokemon.id

    def test_get_pokemon_stats(self, db, pokemon):
        factory = APIRequestFactory()
        request = factory.get('/pokemon/{pokemon.name}')
        view = PokemonView.as_view()

        response = view(request, name=pokemon.name)

        stats_attributes = (
            'hp',
            'speed',
            'defense',
            'attack',
            'special_defence',
            'special_attack'
        )
        for attribute in stats_attributes:
            assert response.data['base_stats'][attribute] == getattr(pokemon.base_stats, attribute)
