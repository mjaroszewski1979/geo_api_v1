# Import TestCase and Client for testing and making requests
from django.test import TestCase, Client
# Import reverse and resolve for URL handling
from django.urls import reverse, resolve
# Import UserCreationForm for user registration form
from django.contrib.auth.forms import UserCreationForm
# Import User model for creating test users
from django.contrib.auth.models import User

# Import views from 'geo' app
from geo import views
# Import Geolocation model from 'geo' app
from geo.models import Geolocation
# Import URL configurations from 'geo_api'
from geo_api import urls


# Establishing fixtures to handle especially expensive setup operations for all of the tests within a module
def setUpModule():
    """
    Set up function executed once before any tests in this module.

    Sets up a test client, creates and logs in a test user for authentication purposes.
    """
    # Instantiate a test client
    client = Client()
    # Create a test user
    user = User.objects.create_user(username='maciej', password='jaroszewski123')
    # Save the test user
    user.save()
    # Log in the test user using the client
    client.login(username='maciej', password='jaroszewski123')

class CreateUserTest(TestCase):
    """
    Test case for testing create_user view.
    """

    def test_create_user_url_is_resolved(self):
        """
        Test URL resolution for create-user endpoint.
        """
        
        url = reverse('create-user')
        self.assertEquals(resolve(url).func, views.create_user)

    def test_create_user_get(self):
        """
        Test GET request to create-user endpoint.
        """
        
        response = self.client.get(reverse('create-user'))

        # Assert response status code is 200 (OK)
        self.assertContains(response, 'GEO API', status_code=200)

        # Assert the 'index.html' template is used
        self.assertTemplateUsed(response, 'index.html')

        # Assert UserCreationForm instance is present in the context
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_create_user_post(self):
        """
        Test POST request to create-user endpoint.
        """
        data = {
            'username' : 'mjaro',
            'password1' : 'jaroszewski123456',
            'password2' : 'jaroszewski123456'
        }
        response = self.client.post(reverse('create-user'), data, follow=True)
        all_users = User.objects.all()

        # Assert response status code is 401 (Unauthorized)
        self.assertEquals(response.status_code, 401)

        # Assert there are two users in the database
        self.assertEquals(all_users.count(), 2)

        # Assert specific error message is present in response content
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)

class GeoDetailTest(TestCase):
    """
    Test case for testing geo-detail view.
    """

    def test_geo_detail_url_is_resolved(self):
        """
        Test URL resolution for geo-detail endpoint.
        """
        
        url = reverse('geo-detail', args=('100.100.200.11', ))
        self.assertEquals(resolve(url).func, views.geo_detail)

    def test_geo_detail_get_without_authentication(self):
        """
        Test GET request to geo-detail endpoint without authentication.
        """
        
        response = self.client.get(reverse('geo-detail', args=('100.100.200.11', )))

        # Assert response status code is 401 (Unauthorized)
        self.assertEquals(response.status_code, 401)

        # Assert specific error message is present in response content
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)

class GeoCreate(TestCase):
    """
    Test case for testing geo-create view.
    """

    def test_geo_create_url_is_resolved(self):
        """
        Test URL resolution for geo-create endpoint.
        """
        
        url = reverse('geo-create')
        self.assertEquals(resolve(url).func, views.geo_create)

    def test_geo_create_get_without_authentication(self):
        """
        Test GET request to geo-create endpoint without authentication.
        """
        
        response = self.client.get(reverse('geo-create'))

        # Assert response status code is 401 (Unauthorized)
        self.assertEquals(response.status_code, 401)

        # Assert specific error message is present in response content
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)
        
class GeoDeleteTest(TestCase):
    """
    Test case for testing geo-delete view.
    """

    def test_geo_delete_url_is_resolved(self):
        """
        Test URL resolution for geo-delete endpoint.
        """

        
        url = reverse('geo-delete', args=('100.100.200.11', ))
        self.assertEquals(resolve(url).func, views.geo_delete)

    def test_geo_delete_get_without_authentication(self):
        """
        Test GET request to geo-delete endpoint without authentication.
        """

        
        response = self.client.get(reverse('geo-delete', args=('100.100.200.11', )))

        # Assert response status code is 401 (Unauthorized)
        self.assertEquals(response.status_code, 401)

        # Assert specific error message is present in response content
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)
        
class GeolocationTest(TestCase):
    """
    Test case for testing Geolocation model.
    """

    def test_geolocation_model(self):
        """
        Test the Geolocation model.
        """
        
        geo = Geolocation(
        ip = '123.456.789',
        longitude = '12,1234567',
        latitude = '56,128976'
        )
        geo.save()
        geo_all = Geolocation.objects.all()

        # Assert geo object is not None
        self.assertIsNotNone(geo)

        # Assert there is one object in the Geolocation model
        self.assertEquals(geo_all.count(), 1)

        # Assert the IP attribute of the geo object is correctly represented as a string
        self.assertEquals(geo.ip, str(geo))
        
class ApiTokenTest(TestCase):
    """
    Test case for testing api-token view.
    """

    def test_api_token_url_is_resolved(self):
        """
        Test URL resolution for api-token endpoint.
        """
        
        url = reverse('api-token')
        self.assertEquals(resolve(url).func.view_class, urls.TokenObtainPairView)

        
    def test_api_token_post(self):
        """
        Test POST request to api-token endpoint.
        """
        
        data = {
            'username' : 'maciej',
            'password' : 'jaroszewski123'
        }
        response = self.client.post(reverse('api-token'), data)

        # Assert response status code is 200 (OK)
        self.assertEquals(response.status_code, 200)
        
class ApiTokenRefresh(TestCase):
    """
    Test case for testing api-token-refresh view.
    """

    def test_api_token_refresh_url_is_resolved(self):
        """
        Test URL resolution for api-token-refresh endpoint.
        """
        
        url = reverse('api-token-refresh')
        self.assertEquals(resolve(url).func.view_class, urls.TokenRefreshView)









    
