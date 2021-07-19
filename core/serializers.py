from rest_framework import serializers

from .models import Pokemon, BaseStat


class EvolutionSerializer(serializers.Serializer):
    name = serializers.CharField()
    evolution_id = serializers.CharField()
    evolution_type = serializers.CharField()


class BaseStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseStat
        fields = (
            "hp",
            "speed",
            "defense",
            "attack",
            "special_defence",
            "special_attack",
        )


class PokemonSerializer(serializers.ModelSerializer):
    base_stats = BaseStatSerializer()
    evolutions = EvolutionSerializer(source="get_evolutions", many=True)

    class Meta:
        model = Pokemon
        fields = ["id", "name", "base_stats", "evolutions"]
