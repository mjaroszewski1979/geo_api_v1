# Django imports for defining database models.
from django.db import models


class Geolocation(models.Model):
    """
    Model representing a geolocation entry with an IP address, longitude, and latitude.
    """

    # CharField for storing the IP address. This field is unique for each geolocation entry.
    ip = models.CharField(max_length=50, unique=True)
    # CharField for storing the longitude of the geolocation.
    longitude = models.CharField(max_length=50)
    # CharField for storing the latitude of the geolocation.
    latitude = models.CharField(max_length=50)


    def __str__(self):
        """
        Return a string representation of the geolocation entry.
        This method returns the IP address of the geolocation.
        """
        return self.ip
