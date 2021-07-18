from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView


from .serializers import PokemonSerializer
from .models import Pokemon



class PokemonView(RetrieveAPIView):
    queryset = Pokemon.objects.all()
    lookup_field = 'name'
    serializer_class = PokemonSerializer
