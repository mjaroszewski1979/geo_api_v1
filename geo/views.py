import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import GeoIpSerializer, GeoSerializer
from .models import Geolocation


@api_view(['GET'])
def geoDetail(request, pk):
	geo = Geolocation.objects.get(ip=pk)
	serializer = GeoSerializer(geo, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def geoCreate(request):
    serializer = GeoIpSerializer(data=request.data)
    if serializer.is_valid():
        ip = serializer.data['ip']
        fields = 'longitude,latitude,ip'
        response = requests.get('http://api.ipstack.com/' + ip + '?access_key=cce8aa93f5ee3af0f4698023b2bc1f13&fields=' + fields)
        response_json = response.json()
        if response_json['error']['info']:
            error = response_json['error']['info']
            return Response(error)
        else:
            longitude = response_json['longitude']
            latitude = response_json['latitude']
            new_geo = Geolocation.objects.create(ip=ip, longitude=longitude, latitude=latitude)
            new_geo.save()
            return Response('Geolocation added!')
    else:
        return Response('Please try different ip address')

@api_view(['DELETE', 'GET'])
def geoDelete(request, pk):
	geo = Geolocation.objects.get(ip=pk)
	geo.delete()

	return Response('Geolocation succsesfully deleted!')
