from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from . import models


class EvolutionPokemonSerializer(serializers.ModelSerializer):
    evolve_to = RecursiveField(allow_null=True, many=True)

    class Meta:
        fields = ["id", "name", "evolve_to"]
        model = models.Pokemon


class DeevolutionPokemonSerializer(serializers.ModelSerializer):
    evolve_from = RecursiveField(allow_null=True)

    class Meta:
        fields = ["id", "name", "evolve_from"]
        model = models.Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    evolve_to = EvolutionPokemonSerializer(allow_null=True, many=True)
    evolve_from = DeevolutionPokemonSerializer(allow_null=True)

    class Meta:
        fields = [
            "id",
            "name",
            "height",
            "weight",
            "evolve_to",
            "evolve_from",
            "stats",
        ]
        model = models.Pokemon
