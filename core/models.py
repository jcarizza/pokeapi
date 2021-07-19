from django.db import models


class Evolution(models.Model):
    name = models.CharField(max_length=300)
    evolution_id = models.IntegerField()

    def evolution_type(self, pokemon_name):
        evolutions = list(Evolution.objects.filter(pokemons__id__in=[p.id for p in self.pokemons.all()]).values_list('name', flat=True))
        this_evo = evolutions.index(self.name)
        poke_evo = evolutions.index(pokemon_name)
        if this_evo < poke_evo:
            return 'Preevolution'
        elif this_evo > poke_evo:
            return 'Evolution'
        else:
            return 'ACTUAL'


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
    base_stats = models.ForeignKey(BaseStat, related_name='pokemon', on_delete=models.CASCADE)
    evolutions = models.ManyToManyField(Evolution, related_name='pokemons')
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)


    @property
    def get_evolutions(self):
        evolutions = [
            {
                'name': evo.name,
                'evolution_id': evo.id,
                'evolution_type': evo.evolution_type(self.name)
            }
        for evo in self.evolutions.all()]

        return [evo for evo in evolutions if evo['evolution_type'] != 'ACTUAL']
