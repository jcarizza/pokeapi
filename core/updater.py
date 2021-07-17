import requests

BASE_API = "https://pokeapi.co/api/v2"
ENDPOINT_POKEMON = "{BASE_API}/pokemon/{name}"


class BaseReader:
    url = ""

    def get(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response


class PokemonResponse:
    pass


class PokemonReader(BaseReader):
    def __init__(self, _id, *args, **kwagrs):
        self.url = f"{BASE_API}/pokemon/pokemon/{_id}"


class EvolutionChainResponse:

    @classmethod
    def parse_response(cls, response):
        data = response.json()
        evolutions = cls.read_evolutions(data)

    @classmethod
    def read_evolutions(cls, data, evolutions=None):

        evo = {}
        if evolutions is None:
            evolutions = []
            data = data['chain']

        evo['name'] = data['species']['name']
        evolutions.append(evo)

        if len(data['evolves_to']) == 0:
            return evolutions


        return cls.read_evolutions(data['evolves_to'][0], evolutions)





class EvolutionChainReader(BaseReader):

    def __init__(self, _id, *args, **kwargs):
        self.url = f"{BASE_API}/evolution-chain/{_id}/"

    def get(self):
        response = super().get()
        EvolutionChainResponse.parse_response(response)

