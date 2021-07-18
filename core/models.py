from django.db import models


class Evolution(models.Model):
    name = models.CharField(max_length=300)
    evolution_id = models.IntegerField()


class BaseStat(models.Model):
    hp = models.IntegerField()
    speed = models.IntegerField()
    defense = models.IntegerField()
    attack = models.IntegerField()
    special_defence = models.IntegerField()
    special_attack = models.IntegerField()


class Pokemon(models.Model):
    pokemon_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=300)
    base_stats = models.ForeignKey(BaseStat, related_name='stats', on_delete=models.CASCADE)
    evolutions = models.ManyToManyField(Evolution, related_name='evolutions')
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
