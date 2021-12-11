from rest_framework import serializers
from .models import Geolocation

class GeoIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('ip',)

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = '__all__'
