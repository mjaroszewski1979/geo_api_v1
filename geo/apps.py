# Import AppConfig from Django's apps module
from django.apps import AppConfig


class GeoConfig(AppConfig):
    """
    Configuration class for the 'geo' Django app.
    """
    
    # Define the default_auto_field for models
    default_auto_field = 'django.db.models.BigAutoField'
    # Specify the name of the Django app 'geo'
    name = 'geo'
