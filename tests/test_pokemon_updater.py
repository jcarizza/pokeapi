from unittest.mock import MagicMock

import httpretty
from django.conf import settings

from core.models import Pokemon, Evolution, BaseStat
from core.updater import PokemonInfoHandler


def load_mocked_response_file(name):
    with open(name, "rb") as f:
        data = f.read()
    return data


def test_update_evolution_chain(db):
    httpretty.enable(verbose=True, allow_net_connect=False)

    for _id in [172, 25, 26]:
        httpretty.register_uri(
            httpretty.GET,
            f"{settings.BASE_API}/pokemon-species/{_id}/",
            body=load_mocked_response_file(
                f"{settings.BASE_DIR}/tests/mocked_responses"
                f"/pokemon_species_{_id}.json"
            ),
            content_type="application/json",
        )

    for name in ["pichu", "pikachu", "raichu"]:
        httpretty.register_uri(
            httpretty.GET,
            f"{settings.BASE_API}/pokemon/{name}/",
            body=load_mocked_response_file(
                f"{settings.BASE_DIR}/tests/mocked_responses/"
                f"pokemon_{name}.json"
            ),
            content_type="application/json",
        )

    chain_id = 10
    httpretty.register_uri(
        httpretty.GET,
        f"{settings.BASE_API}/evolution-chain/{chain_id}/",
        body=load_mocked_response_file(
            f"{settings.BASE_DIR}/tests/mocked_responses/"
            f"evolution_chain_10.json"
        ),
        content_type="application/json",
    )

    PokemonInfoHandler.retrieve_and_store_pokemon_info(chain_id)

    assert len(Pokemon.objects.all()) == 3
    assert len(Evolution.objects.all()) == 3
    assert len(BaseStat.objects.all()) == 3



class TestPokemonInfoHandler:
    def test_retrieve_and_store_pokemon_info(self, mocker):

        # Create mocks
        BASE_PATH = PokemonInfoHandler.__module__
        pokemons_dict_mock = MagicMock()
        evolutions_dict_mock = MagicMock()
        base_stat_object_mock = MagicMock()
        pokemon_object_mock = MagicMock()
        evolution_chain_reader_mock = mocker.patch(f"{BASE_PATH}.EvolutionChainReader")
        evolution_mock = mocker.patch(f"{BASE_PATH}.Evolution")
        base_stat_mock = mocker.patch(f"{BASE_PATH}.BaseStat")
        pokemon_mock = mocker.patch(f"{BASE_PATH}.Pokemon")

        # The evolution chain reader will return a list of pokemons and evolutions
        evolution_chain_reader_mock.return_value.get.return_value = [[pokemons_dict_mock], [evolutions_dict_mock]]

        # Evolution gets created
        created_evolution = MagicMock()
        evolution_mock.objects.update_or_create.return_value = [created_evolution, True]

        # Now base stat and pokemons are created
        base_stat_mock.objects.create.return_value = base_stat_object_mock
        pokemon_mock.objects.update_or_create.return_value = [pokemon_object_mock, True]

        evolution_chain_id = 10
        PokemonInfoHandler.retrieve_and_store_pokemon_info(evolution_chain_id)

        # Evolution chain reads from API
        evolution_chain_reader_mock.assert_called_with(evolution_chain_id)
        evolution_chain_reader_mock.return_value.get.assert_called()

        # The evolutions objects are created
        evolution_mock.objects.update_or_create.assert_called()

        # Pokemons and base stats are created
        pokemon_mock.objects.update_or_create.assert_called()
        base_stat_mock.objects.create.assert_called()
        pokemon_object_mock.evolutions.add.assert_called_with(created_evolution)


