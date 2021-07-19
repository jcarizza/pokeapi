import pytest

from rest_framework.test import APIRequestFactory

from factories import PokemonFactory, EvolutionFactory
from core.views import PokemonView


@pytest.fixture
def pokemon():
    return PokemonFactory.create()

@pytest.fixture
def evolution_factory():
    return EvolutionFactory


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

    @pytest.mark.parametrize(
        'pokemon_actual_evolution, evo_type_0, evo_type_1',[
            (0, (0, 'Evolution'), (1, 'Evolution')),
            (1, (0, 'Preevolution'), (1, 'Evolution')),
            (2, (0, 'Preevolution'), (1, 'Preevolution')),
    ])
    def test_get_pokemon_evolutions(self, db, pokemon, evolution_factory, pokemon_actual_evolution, evo_type_0, evo_type_1):
        # Create 3 evolutions for this pokemon and make it evolve
        evolutions = [evolution_factory.create() for n in range(3)]
        evolutions[pokemon_actual_evolution].name = pokemon.name
        evolutions[pokemon_actual_evolution].save()

        pokemon.evolutions.add(evolutions[0])
        pokemon.evolutions.add(evolutions[1])
        pokemon.evolutions.add(evolutions[2])

        factory = APIRequestFactory()
        request = factory.get('/pokemon/{pokemon.name}')
        view = PokemonView.as_view()

        response = view(request, name=pokemon.name)


        actual_evolution_type_0 = response.data['evolutions'][evo_type_0[0]]['evolution_type']
        actual_evolution_type_1 = response.data['evolutions'][evo_type_1[0]]['evolution_type']
        expected_evolution_type_0 = evo_type_0[1]
        expected_evolution_type_1 = evo_type_1[1]
        assert actual_evolution_type_0 == expected_evolution_type_0
        assert actual_evolution_type_1 == expected_evolution_type_1


