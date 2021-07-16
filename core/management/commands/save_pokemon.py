from core.updater import EvolutionChainReader

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Save Pokemon info'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **options):
        evolution_id = options['id']
        evolution_chain_reader = EvolutionChainReader(evolution_id)
        print(evolution_chain_reader.get())

