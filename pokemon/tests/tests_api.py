from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pokemon import models

EXPECTED_RESPONSE = {
    "count": 6,
    "next": "http://testserver/api/pokemon/?limit=2&offset=2",
    "previous": None,
    "results": [
        {
            "id": 4,
            "name": "charmander",
            "height": 6.0,
            "weight": 6.0,
            "evolve_to": [
                {
                    "id": 5,
                    "name": "charmeleon",
                    "evolve_to": [
                        {"id": 6, "name": "charizard", "evolve_to": []},
                        {
                            "id": 10034,
                            "name": "charizard-mega-x",
                            "evolve_to": [],
                        },
                        {
                            "id": 10035,
                            "name": "charizard-mega-y",
                            "evolve_to": [],
                        },
                        {
                            "id": 10187,
                            "name": "charizard-gmax",
                            "evolve_to": [],
                        },
                    ],
                }
            ],
            "evolve_from": None,
            "stats": [
                {
                    "base_stat": 39,
                    "effort": 0,
                    "stat": {
                        "name": "hp",
                        "url": "https://pokeapi.co/api/v2/stat/1/",
                    },
                },
                {
                    "base_stat": 52,
                    "effort": 0,
                    "stat": {
                        "name": "attack",
                        "url": "https://pokeapi.co/api/v2/stat/2/",
                    },
                },
                {
                    "base_stat": 43,
                    "effort": 0,
                    "stat": {
                        "name": "defense",
                        "url": "https://pokeapi.co/api/v2/stat/3/",
                    },
                },
                {
                    "base_stat": 60,
                    "effort": 0,
                    "stat": {
                        "name": "special-attack",
                        "url": "https://pokeapi.co/api/v2/stat/4/",
                    },
                },
                {
                    "base_stat": 50,
                    "effort": 0,
                    "stat": {
                        "name": "special-defense",
                        "url": "https://pokeapi.co/api/v2/stat/5/",
                    },
                },
                {
                    "base_stat": 65,
                    "effort": 1,
                    "stat": {
                        "name": "speed",
                        "url": "https://pokeapi.co/api/v2/stat/6/",
                    },
                },
            ],
        },
        {
            "id": 5,
            "name": "charmeleon",
            "height": 11.0,
            "weight": 11.0,
            "evolve_to": [
                {"id": 6, "name": "charizard", "evolve_to": []},
                {"id": 10034, "name": "charizard-mega-x", "evolve_to": []},
                {"id": 10035, "name": "charizard-mega-y", "evolve_to": []},
                {"id": 10187, "name": "charizard-gmax", "evolve_to": []},
            ],
            "evolve_from": {
                "id": 4,
                "name": "charmander",
                "evolve_from": None,
            },
            "stats": [
                {
                    "base_stat": 39,
                    "effort": 0,
                    "stat": {
                        "name": "hp",
                        "url": "https://pokeapi.co/api/v2/stat/1/",
                    },
                },
                {
                    "base_stat": 52,
                    "effort": 0,
                    "stat": {
                        "name": "attack",
                        "url": "https://pokeapi.co/api/v2/stat/2/",
                    },
                },
                {
                    "base_stat": 43,
                    "effort": 0,
                    "stat": {
                        "name": "defense",
                        "url": "https://pokeapi.co/api/v2/stat/3/",
                    },
                },
                {
                    "base_stat": 60,
                    "effort": 0,
                    "stat": {
                        "name": "special-attack",
                        "url": "https://pokeapi.co/api/v2/stat/4/",
                    },
                },
                {
                    "base_stat": 50,
                    "effort": 0,
                    "stat": {
                        "name": "special-defense",
                        "url": "https://pokeapi.co/api/v2/stat/5/",
                    },
                },
                {
                    "base_stat": 65,
                    "effort": 1,
                    "stat": {
                        "name": "speed",
                        "url": "https://pokeapi.co/api/v2/stat/6/",
                    },
                },
            ],
        },
    ],
}


class PokemonApiTests(APITestCase):
    def setUp(self):
        stats = [
            {
                "base_stat": 39,
                "effort": 0,
                "stat": {
                    "name": "hp",
                    "url": "https://pokeapi.co/api/v2/stat/1/",
                },
            },
            {
                "base_stat": 52,
                "effort": 0,
                "stat": {
                    "name": "attack",
                    "url": "https://pokeapi.co/api/v2/stat/2/",
                },
            },
            {
                "base_stat": 43,
                "effort": 0,
                "stat": {
                    "name": "defense",
                    "url": "https://pokeapi.co/api/v2/stat/3/",
                },
            },
            {
                "base_stat": 60,
                "effort": 0,
                "stat": {
                    "name": "special-attack",
                    "url": "https://pokeapi.co/api/v2/stat/4/",
                },
            },
            {
                "base_stat": 50,
                "effort": 0,
                "stat": {
                    "name": "special-defense",
                    "url": "https://pokeapi.co/api/v2/stat/5/",
                },
            },
            {
                "base_stat": 65,
                "effort": 1,
                "stat": {
                    "name": "speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/",
                },
            },
        ]
        charmander = models.Pokemon.objects.create(
            id=4,
            name="charmander",
            height=6.0,
            weight=6.0,
            evolve_from=None,
            stats=stats,
        )
        charmeleon = models.Pokemon.objects.create(
            id=5,
            name="charmeleon",
            height=11.0,
            weight=11.0,
            evolve_from=charmander,
            stats=stats,
        )
        models.Pokemon.objects.create(
            id=6,
            name="charizard",
            height=17.0,
            weight=17.0,
            evolve_from=charmeleon,
            stats=stats,
        )
        models.Pokemon.objects.create(
            id=10034,
            name="charizard-mega-x",
            height=17.0,
            weight=17.0,
            evolve_from=charmeleon,
            stats=stats,
        )
        models.Pokemon.objects.create(
            id=10035,
            name="charizard-mega-y",
            height=17.0,
            weight=17.0,
            evolve_from=charmeleon,
            stats=stats,
        )
        models.Pokemon.objects.create(
            id=10187,
            name="charizard-gmax",
            height=280.0,
            weight=280.0,
            evolve_from=charmeleon,
            stats=stats,
        )

    def test_list_url(self):
        """
        Ensure the paginate endpoint is available.
        """
        url = reverse("pokemon-list")
        self.assertEqual(url, "/api/pokemon/")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_url(self):
        """
        Ensure the detail endpoint is available.
        """
        url = reverse("pokemon-detail", args=["pikachu"])
        self.assertEqual(url, "/api/pokemon/pikachu/")

    def test_pokemon_list(self):
        """
        Ensure the endpoint returns the expected response
        """

        url = reverse("pokemon-list")
        with self.assertNumQueries(5):
            response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data["count"], 6)
        self.assertEqual(data, EXPECTED_RESPONSE)

    def test_pokemon_must_not_exist(self):
        """
        Ensure the response must be 404 when the pokemon does not exists
        """
        url = reverse("pokemon-detail", args=["pikachu"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_pokemon_must_exist(self):
        """
        Ensure the endpoint returns the expected response
        """
        url = reverse("pokemon-detail", args=["charmeleon"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
