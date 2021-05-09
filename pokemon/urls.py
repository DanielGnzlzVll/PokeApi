from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"pokemon", views.PokemonViewSet, basename="pokemon")

urlpatterns = [path("", include(router.urls))]
