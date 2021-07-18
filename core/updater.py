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


class PokemonSpeciesReader(BaseReader):
    def __init__(self, *args, _id=None, url=None, **kwargs):
        self.url = url
        if url is None:
            self.url = f"{BASE_API}/pokemon-species/{_id}"

class PokemonSpeciesResponse:
    @staticmethod
    def parse_response(data):
        return data.json()


class EvolutionChainResponse:

    @classmethod
    def parse_response(cls, response):
        pokemon_data = {}
        response_data = response.json()
        evolutions = cls.read_evolutions(response_data)


        pokemon_data['evolutions'] = evolutions

        return pokemon_data

    @classmethod
    def read_info_for_every_evolution(cls, evolutions):
        for evo in evolutions:
            data = PokemonReader(url)
            poke['name'] = data.name
            poke['height'] = data.height

    @classmethod
    def get_pokemon_specie_info(cls, url):
        response = PokemonSpeciesReader(url=url).get()
        response_data = PokemonSpeciesResponse.parse_response(response)
        return response_data


    @classmethod
    def read_evolutions(cls, data, evolutions=None, is_pos_evolution=None, current_evo=None):

        evo = {}
        if evolutions is None:
            evolutions = []
            data = data['chain']

        species_data = cls.get_pokemon_specie_info(data['species']['url'])

        evo['name'] = data['species']['name']
        evo['id'] = species_data['id']
        evolutions.append(evo)

        if len(data['evolves_to']) == 0:
            return evolutions


        return cls.read_evolutions(data['evolves_to'][0], evolutions)





class EvolutionChainReader(BaseReader):

    def __init__(self, _id, *args, **kwargs):
        self.url = f"{BASE_API}/evolution-chain/{_id}/"

    def get(self):
        response = super().get()
        return EvolutionChainResponse.parse_response(response)

