from rest_framework import serializers

from .models import Pokemon, BaseStat

class BaseStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseStat
        fields = (
            'hp',
            'speed',
            'defense',
            'attack',
            'special_defence',
            'special_attack'
        )

class PokemonSerializer(serializers.ModelSerializer):
    base_stats = BaseStatSerializer()

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'base_stats']
