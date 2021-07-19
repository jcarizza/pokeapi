from core.updater import PokemonInfoHandler

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Save Pokemon and Evolution info."

    def add_arguments(self, parser):
        parser.add_argument("id", type=int)

    def handle(self, *args, **options):
        evolution_chain_id = options["id"]
        PokemonInfoHandler.retrieve_and_store_pokemon_info(evolution_chain_id)
