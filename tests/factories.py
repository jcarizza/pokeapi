import factory
from factory.fuzzy import FuzzyInteger
from core.models import Evolution, BaseStat, Pokemon



class EvolutionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evolution


class BaseStatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model =  BaseStat

    hp = FuzzyInteger(low=1, high=100)
    speed = FuzzyInteger(low=1, high=100)
    defense = FuzzyInteger(low=1, high=100)
    attack = FuzzyInteger(low=1, high=100)
    special_defence = FuzzyInteger(low=1, high=100)
    special_attack = FuzzyInteger(low=1, high=100)


class PokemonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pokemon

    pokemon_id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'pokemon_%s' % n)
    base_stats = factory.SubFactory(BaseStatFactory)
    height = FuzzyInteger(low=1)
    weight = FuzzyInteger(low=1)
