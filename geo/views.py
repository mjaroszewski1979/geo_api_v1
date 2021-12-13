import requests

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .serializers import GeoIpSerializer, GeoSerializer
from .models import Geolocation


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)


            return redirect('geo-create')
    else:
        form = UserCreationForm()

    return render(request, 'index.html', {'form': form})


@api_view(['GET'])
def geo_detail(request, pk):
	geo = Geolocation.objects.get(ip=pk)
	serializer = GeoSerializer(geo, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def geo_create(request):
    serializer = GeoIpSerializer(data=request.data)
    if serializer.is_valid():
        ip = serializer.data['ip']
        fields = 'longitude,latitude,ip'
        response = requests.get('http://api.ipstack.com/' + ip + '?access_key=cce8aa93f5ee3af0f4698023b2bc1f13&fields=' + fields)
        if response.status_code == 200:
            try:
                response_json = response.json()
                longitude = response_json['longitude']
                latitude = response_json['latitude']
                new_geo = Geolocation.objects.create(ip=ip, longitude=longitude, latitude=latitude)
                new_geo.save()
                return Response('Geolocation added!')
            except KeyError:
                return Response(
                    {
                        "Error" : "Invalid IP address"
                    }
                )
        else:
            return Response(
                {
                    "Invalid status code" : response.status_code
                }
            )
    else:
        return Response(
            {
                "Error" : "Please choose different IP address"
            }
        )

@api_view(['GET', 'DELETE'])
def geo_delete(request, pk):
	geo = Geolocation.objects.get(ip=pk)
	geo.delete()

	return Response('Geolocation succsesfully deleted!')
