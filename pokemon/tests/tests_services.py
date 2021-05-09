import json
import os

from django.test import TestCase
from pokemon import models, services

DATA_DIR = os.path.join(os.path.dirname(__file__), "api_data")


def test_fetcher(url):
    file_name = url.split("/api/")[-1].replace("/", "_") + ".json"
    file_name = os.path.join(DATA_DIR, file_name)
    with open(file_name) as file:
        data = json.loads(file.read())
    return data


class PokemonCommandTests(TestCase):
    def test_pokemon_command(self):
        """
        Ensure charmander evolution chain is handle properly.
        """
        services.fetch_and_storage_pokemons_from_evolution_chain(2, fetcher=test_fetcher)
        self.assertEqual(models.Pokemon.objects.all().count(), 6)
        self.assertEqual(
            models.Pokemon.objects.filter(name="charmander").count(), 1
        )
        self.assertEqual(
            models.Pokemon.objects.filter(name="charmeleon").count(), 1
        )
        self.assertEqual(
            models.Pokemon.objects.filter(name="charizard").count(), 1
        )
        self.assertEqual(
            models.Pokemon.objects.filter(name="charizard-mega-x").count(), 1
        )
        self.assertEqual(
            models.Pokemon.objects.filter(name="charizard-mega-y").count(), 1
        )
        self.assertEqual(
            models.Pokemon.objects.filter(name="charizard-gmax").count(), 1
        )

        charmeleon = models.Pokemon.objects.get(name="charmeleon")
        self.assertEqual(charmeleon.evolve_from.name, "charmander")
        self.assertEqual(charmeleon.evolve_to.all().count(), 4)










