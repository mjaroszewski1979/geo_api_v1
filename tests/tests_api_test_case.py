# Import User model for creating test user
from django.contrib.auth.models import User
# Import reverse function for generating URLs
from django.urls import reverse

# Import APIClient for making test requests
from rest_framework.test import APIClient
# Import status constants for HTTP status codes
from rest_framework import status
# Import APITestCase for testing API endpoints
from rest_framework.test import APITestCase

# Import Geolocation model from the 'geo' app
from geo.models import Geolocation

# Creating parent test class that inherits from APITestCase
class TestCaseBase(APITestCase):
    """
    Base test case class that sets up authentication for API testing using APIClient.
    """
    @property
    def bearer_token(self):
        """
        Property method to retrieve Bearer token for authenticated requests.

        Returns:
            dict: HTTP Authorization header with Bearer token.
        """

        username = 'mjaro1245'
        password = 'jaroszewski987'
        
        # Instantiate APIClient for making test requests
        client = APIClient()
        
        # Generate URL for obtaining API token
        url = reverse('api-token')
        
        # Create and save a test user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        # Log in the test user using the APIClient
        self.client.login(username=username, password=password)
        
        # Send a POST request to obtain the access token
        resp = client.post(url, {'username': username, 'password': password}, format='json')

        # Extract the Bearer token from the response data
        token = resp.data['access']

        # Return HTTP Authorization header with Bearer token
        return {"HTTP_AUTHORIZATION":f'Bearer {token}'}

class TestGeoAPI(TestCaseBase):
    """
    Test case class for testing Geo API endpoints.
    """
    
    def setUp(self):
        self.geo = Geolocation(
            ip = '134.201.250.155',
            longitude = '12,1234567',
            latitude = '56,128976'
        )
        self.geo.save()

    def test_get_geo_detail(self):
        """
        Test method for testing geo_detail endpoint with valid credentials.
        """
        url = reverse('geo-detail', args=(self.geo.ip, ))
        response = self.client.get(url, **self.bearer_token)

        # Assert HTTP status code is 200 (OK)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Assert the IP address returned in response data matches the expected IP
        self.assertTrue(self.geo.ip in response.data['ip'])

    def test_delete_geo(self):
        """
        Test method for testing geo_delete endpoint with valid credentials.
        """
        
        url = reverse('geo-delete', args=(self.geo.ip, ))
        response = self.client.get(url, **self.bearer_token)

        # Assert HTTP status code is 200 (OK)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Assert the response data matches the success message for deletion
        self.assertEquals({'Succes': 'Geolocation succsesfully deleted!'}, response.data)
    
    def test_create_geo(self):
        """
        Test method for testing geo_create endpoint with valid credentials.
        """
        
        data = {"ip" : "109.173.214.104"}
        url = reverse('geo-create')
        response = self.client.post(url, data, **self.bearer_token)

        # Assert HTTP status code is 200 (OK)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Assert the success message is present in the response data
        self.assertTrue('Geolocation added!' in response.data)











