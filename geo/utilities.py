# Import the os module for interacting with the operating system
import os
# Import the requests library for making HTTP requests
import requests
# Import the Geolocation model from the current application
from .models import Geolocation

def get_geo(ip, api_key = os.environ.get('API_KEY')):
    """
    Retrieve geolocation data for a given IP address using an external API service.

    Parameters:
        ip (str): A valid IP address.
        api_key (str): The API key for authenticating with the external API service (default is retrieved from environment variables).

    Returns:
        dict: A JSON message indicating success or error, depending on the user input and response status codes.
    """

    # Specify the fields to be retrieved from the API response
    fields = 'longitude,latitude,ip'
    # Make the GET request to the API
    response = requests.get('http://api.ipstack.com/' + str(ip) + '?access_key=' + str(api_key) + '&fields=' + fields)
    # Parse the response JSON
    response_json = response.json()

    # Check if the response status code indicates success
    if response.status_code == 200:
        # Check if the IP field is present in the response JSON
        if response_json.get('ip') != None:
            # Retrieve the longitude from the response JSON
            longitude = response_json.get('longitude')
            # Retrieve the latitude from the response JSON
            latitude = response_json.get('latitude')
            # Define a success message
            success_msg = { 'Success' : 'Geolocation added!' }
            # Create a new Geolocation object
            new_geo = Geolocation.objects.create(ip=str(ip), longitude=longitude, latitude=latitude)
            # Save the new Geolocation object to the database
            new_geo.save()
            # Return the success message
            return success_msg
        else:
            # Define the error message as the response JSON
            error_msg = response_json
            # Return the error message
            return error_msg
    else:
        # Return the status code if the response indicates failure
        return response.status_code
