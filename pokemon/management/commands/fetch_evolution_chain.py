from django.core.management.base import BaseCommand
from pokemon import services


class Command(BaseCommand):
    """Get and store the pokemons in the evolution chain 
    with the given id.
    """

    def add_arguments(self, parser):

        parser.add_argument(
            "id", nargs="+", type=int, help="Evolution chain id."
        )

    def handle(self, *args, **options):
        """Get and store the pokemons in the evolution chain 
        with the given id.
        """

        for chain_id in options["id"]:
            services.fetch_and_storage_pokemons_from_evolution_chain(chain_id)
