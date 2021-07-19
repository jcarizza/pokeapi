from pprint import pprint

import requests

BASE_API = "https://pokeapi.co/api/v2"
ENDPOINT_POKEMON = "{BASE_API}/pokemon/{name}"


class BaseReader:
    url = ""

    def get(self):
        response = requests.get(self.url)

        print('=== Mock URL ===')
        print(self.url)
        with open(self.url.replace('/', '_'), 'w+') as f:
            f.write(response.content.decode('utf8'))
        print('=== Mock URL ===')

        response.raise_for_status()
        return response


class PokemonResponse:

    @staticmethod
    def parse_response(response):

        data = response.json()
        stats = {}
        for stat in data['stats']:
            stats[stat['stat']['name']] = stat['base_stat']

        return {
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'id': data['id'],
            'base_stats': {
                'hp': stats['hp'],
                'speed': stats['speed'],
                'defense': stats['defense'],
                'attack': stats['attack'],
                'special_defence': stats['special-defense'],
                'special_attack': stats['special-attack'],
            }
        }


class PokemonReader(BaseReader):
    def __init__(self, name, *args, **kwagrs):
        self.url = f"{BASE_API}/pokemon/{name}"


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
        response_data = response.json()
        evolutions = cls.read_evolutions(response_data)
        pokemons = cls.read_pokemon_info_for_every_evolution(evolutions)

        return (
            pokemons,
            evolutions
        )

    @classmethod
    def read_pokemon_info_for_every_evolution(cls, evolutions):
        pokemons = []
        for evo in evolutions:
            response = PokemonReader(evo['name']).get()
            pokemon_data = PokemonResponse.parse_response(response)
            pokemons.append(pokemon_data)

        return pokemons


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
        breakpoint()
        pokemons, evolutions =  EvolutionChainResponse.parse_response(response)
        pprint(pokemons)
        pprint(evolutions)

