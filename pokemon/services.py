import requests
import django

from pokemon import models


def _do_fetch(url):
    headers = {"content-type": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def fetch_evolution_chain(chain_id, fetcher):
    """
    Get data of a given chain_id.
    """
    url = f"https://pokeapi.co/api/v2/evolution-chain/{chain_id}"
    return fetcher(url)


def fetch_specie(specie_url, fetcher):
    """
    Get Data of a specie.
    """
    return fetcher(specie_url)


def fetch_pokemon(pokemon_url, fetcher):
    """
    Get data of a Pokemon.
    """
    return fetcher(pokemon_url)


def map_data_to_pokemon(data, parent=None):
    """
    Map the data structure provide by pokeapi to a internal ``Pokemon``

    :param data: Data provide by the pokeapi api.
    :type data: ``dict``
    :param parent: Preevolution of the pokemon specie, defaults to None
    :type parent: ``models.Pokemon``, optional
    :return: The extracted pokemon from the provide data.
    :rtype: ``models.Pokemon``
    """
    
    pokemon, _ = models.Pokemon.objects.get_or_create(
        id=data["id"],
        defaults=dict(
            id=data["id"],
            name=data["name"],
            height=data["height"],
            weight=data["height"],
            stats=data["stats"],
            evolve_from=parent,
        ),
    )
    return pokemon


def create_pokemon_from_chain(chain, fetcher, parent=None):
    """
    Given a evolution chain extrated from `https://pokeapi.co/`.

    :param chain: All data info provide by the pokeapi.
    :type chain: ``dict``
    :param fetcher: Function to do the fetch.
    :type fetcher: ``Callable``, optional
    :param parent: Preevolution of the pokemon specie, defaults to None
    :type parent: ``models.Pokemon``, optional
    """
    
    specie_url = chain["species"]["url"]
    specie_data = fetch_specie(specie_url, fetcher)
    pokemon_list = []
    for pokemon in specie_data["varieties"]:
        pokemon_url = pokemon["pokemon"]["url"]
        pokemon_data = fetch_pokemon(pokemon_url, fetcher)
        pokemon = map_data_to_pokemon(pokemon_data, parent=parent)
        pokemon_list.append(pokemon)

    for children in chain.get("evolves_to", []):
        # In case tha a pokemon has multiples varities, the evolutions
        # are marked as evolution of first varietie.
        parent = pokemon_list[0]
        create_pokemon_from_chain(children, fetcher, parent=parent)


def fetch_and_storage_pokemons_from_evolution_chain(chain_id, fetcher=None):
    """
    Fetch a evolution chain from `https://pokeapi.co/` and storage the related
    pokemons.

    :param chain_id: The id of the chain.
    :type chain_id: ``int``
    :param fetcher: Function to do the fetch, defaults to None
    :type fetcher: ``Callable``, optional
    """
    if not fetcher:
        fetcher = _do_fetch

    data = fetch_evolution_chain(chain_id, fetcher)
    if data:
        baby = data["chain"]
        create_pokemon_from_chain(baby, fetcher)
