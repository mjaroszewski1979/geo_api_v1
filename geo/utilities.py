import os
import requests
from .models import Geolocation

def get_geo(ip):
    fields = 'longitude,latitude,ip'
    response = requests.get('http://api.ipstack.com/' + ip + '?access_key=' + os.environ.get('API_KEY') + '&fields=' + fields)
    if response.status_code == 200:
        try:
            response_json = response.json()
            longitude = response_json['longitude']
            latitude = response_json['latitude']
            success_msg = 'Geolocation added!'
            new_geo = Geolocation.objects.create(ip=ip, longitude=longitude, latitude=latitude)
            new_geo.save()
            return success_msg
        except KeyError:
            error_msg = {
                    "Error" : "Invalid IP address"
                    }
            return error_msg
    else:
        status_msg = {
                "Invalid status code" : response.status_code
                }
        return status_msg
