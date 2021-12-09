from rest_framework import serializers
from .models import Geolocation

class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('ip', 'continent_code', 'continent_name', 'country_code', 'continent_code', 'country_name',
                  'region_code', 'region_name', 'city', 'zip', 'latitude', 'longitude')
