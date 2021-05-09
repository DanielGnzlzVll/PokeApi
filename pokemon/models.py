from django.db import models
from django.core.validators import MinValueValidator


class Pokemon(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    height = models.FloatField(validators=[MinValueValidator(0)])
    weight = models.FloatField(validators=[MinValueValidator(0)])
    evolve_from = models.ForeignKey(
        "Pokemon",
        related_name="evolve_to",
        related_query_name="evolve_to_2",
        on_delete=models.CASCADE,
        null=True,
    )
    stats = models.JSONField()

    def __str__(self):
        return self.name
