from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Geolocation
from .serializers import GeolocationSerializer

class GeoView(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
