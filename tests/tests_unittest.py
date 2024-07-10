# Import unittest module for defining unit tests
import unittest
# Import os module for environment variables handling
import os

# Import get_geo function from 'geo.utilities'
from geo.utilities import get_geo

class TestGetGeo(unittest.TestCase):
    """
    Test case for testing the get_geo function.
    """

    def test_get_geo_valid_ip(self):
        """
        Test method for testing get_geo function with a valid IP address and API key.
        """
        
        actual = get_geo('134.201.250.155', os.environ.get('API_KEY'))
        expected = {'Success': 'Geolocation added!'}
        self.assertEquals(actual, expected)

    def test_get_geo_invalid_ip(self):
        """
        Test method for testing get_geo function with an invalid IP address and valid API key.
        """
        
        actual = get_geo('12',  os.environ.get('API_KEY'))
        expected = {'success': False,
                    'error': {'code': 106,
                    'type': 'invalid_ip_address',
                    'info': 'The IP Address supplied is invalid.'}}
        self.assertEquals(actual, expected)

    def test_get_geo_invalid_api_key(self):
        """
        Test method for testing get_geo function with a valid IP address and invalid API key.
        """
        
        actual = get_geo('134.201.250.155', 'invalid')
        expected = {'success': False,
                    'error': {'code': 101,
                    'type': 'invalid_access_key',
                    'info': 'You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]'}}
        self.assertEquals(actual, expected)
