from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase

from geo.models import Geolocation


class TestCaseBase(APITestCase):
    @property
    def bearer_token(self):
        username = 'mjaro1245'
        password = 'jaroszewski987'
        client = APIClient()
        url = reverse('api-token')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        self.client.login(username=username, password=password)
        resp = client.post(url, {'username': username, 'password': password}, format='json')
        token = resp.data['access']
        return {"HTTP_AUTHORIZATION":f'Bearer {token}'}

class TestGeoAPI(TestCaseBase):

    def setUp(self):
        self.geo = Geolocation(
            ip = '134.201.250.155',
            longitude = '12,1234567',
            latitude = '56,128976'
        )
        self.geo.save()

    def test_get_geo_detail(self):
        url = reverse('geo-detail', args=(self.geo.ip, ))
        response = self.client.get(url, **self.bearer_token)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.geo.ip in response.data['ip'])

    def test_delete_geo(self):
        url = reverse('geo-delete', args=(self.geo.ip, ))
        response = self.client.get(url, **self.bearer_token)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals({'Succes': 'Geolocation succsesfully deleted!'}, response.data)

    def test_create_geo(self):
        data = {"ip" : "109.173.214.104"}
        url = reverse('geo-create')
        response = self.client.post(url, data, **self.bearer_token)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue('Geolocation added!' in response.data)











