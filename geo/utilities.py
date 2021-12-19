# Python imports
import os
import requests
# App imports
from .models import Geolocation

<<<<<<< HEAD
def get_geo(ip, api_key = os.environ.get('API_KEY')):
    '''
    This function is using requests and calling an external api service to extract geolocation data for a given ip address
            Parameters:
                    ip (str): A valid ip address
=======

def get_geo(ip):
    '''
    This function is using requests and calling an external api service to extract geolocation data for a given ip address

            Parameters:
                    ip (str): A valid ip address

>>>>>>> ee8166a3b8bf4aaa4a9a9f9975f0fd942f57854e
            Returns:
                    message (json): Success or error message depending on user input and response status codes 
    '''
    fields = 'longitude,latitude,ip'
<<<<<<< HEAD
    response = requests.get('http://api.ipstack.com/' + str(ip) + '?access_key=' + api_key + '&fields=' + fields)
    response_json = response.json()
=======
    response = requests.get('http://api.ipstack.com/' + str(ip) + '?access_key=' + os.environ.get('API_KEY') + '&fields=' + fields)
>>>>>>> ee8166a3b8bf4aaa4a9a9f9975f0fd942f57854e
    if response.status_code == 200:
        if response_json.get('ip') != None:
            longitude = response_json.get('longitude')
            latitude = response_json.get('latitude')
            success_msg = { 'Success' : 'Geolocation added!' }
            new_geo = Geolocation.objects.create(ip=str(ip), longitude=longitude, latitude=latitude)
            new_geo.save()
            return success_msg
        else:
            error_msg = response_json
            return error_msg
    else:
        return response.status_code
