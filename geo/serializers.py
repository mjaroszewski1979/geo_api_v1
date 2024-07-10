# Import serializers from Django REST framework
from rest_framework import serializers
# Import Geolocation model from the current application
from .models import Geolocation

# Define a serializer for the Geolocation model to handle only the IP field
class GeoIpSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Geolocation model, limited to the 'ip' field.
    """
    class Meta:
        """
        Meta class to specify the model and fields to be serialized.
        """

        # Associate this serializer with the Geolocation model
        model = Geolocation
        # Specify that only the 'ip' field should be included in the serialization
        fields = ('ip',)

# Define a serializer for the Geolocation model to handle all fields
class GeoSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Geolocation model, including all fields.
    """
    class Meta:
        """
        Meta class to specify the model and fields to be serialized.
        """

        # Associate this serializer with the Geolocation model
        model = Geolocation
        # Include all fields of the Geolocation model in the serialization
        fields = '__all__'
