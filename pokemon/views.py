from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from . import models, serializers


class PokemonViewSet(ReadOnlyModelViewSet):
    serializer_class = serializers.PokemonSerializer
    lookup_field = "name"

    def get_queryset(self):
        qs = models.Pokemon.objects.all()
        qs = qs.select_related("evolve_from")

        # It's a little tricky, but it avoids many many queries
        # when the pokemon has less than 4 evolutions.
        qs = qs.prefetch_related("evolve_to__evolve_to__evolve_to__evolve_to")
        return qs
