from rest_framework.test import APIRequestFactory


from core.views import PokemonView


class TestPokemonResource:


    def test_get_pokemon(self, db):
        factory = APIRequestFactory()
        request = factory.get('/pokemon/1')
        view = PokemonView.as_view()
        assert view(request, pk=1).status_code == 200
