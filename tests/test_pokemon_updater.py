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
