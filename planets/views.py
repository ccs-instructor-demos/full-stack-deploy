# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Planet
from .serializers import PlanetSerializer


class PlanetViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Planet.objects.all()
        serializer = PlanetSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Planet.objects.all()
        planet = get_object_or_404(queryset, pk=pk)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)
