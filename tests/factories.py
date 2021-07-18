from factory_boy import factory
from .models import Evolution, BaseStat, Pokemon


class EvolutionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evolution


class BaseStatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model =  BaseStat

class PokemonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pokemon
