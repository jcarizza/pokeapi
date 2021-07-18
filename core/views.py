from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView


from .models import Pokemon



class PokemonView(RetrieveAPIView):
    queryset = Pokemon.objects.all()
