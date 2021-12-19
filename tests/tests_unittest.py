<<<<<<< HEAD
# python imports
import unittest

# app imports
from geo.utilities import get_geo

# Testing get_geo function
class TestGetGeo(unittest.TestCase):

    def test_get_geo_valid_ip(self):
        actual = get_geo('134.201.250.155', 'cce8aa93f5ee3af0f4698023b2bc1f13')
        expected = {'Success': 'Geolocation added!'}
        self.assertEquals(actual, expected)

    def test_get_geo_invalid_ip(self):
        actual = get_geo('12', 'cce8aa93f5ee3af0f4698023b2bc1f13')
        expected = {'success': False,
                    'error': {'code': 106,
                    'type': 'invalid_ip_address',
                    'info': 'The IP Address supplied is invalid.'}}
        self.assertEquals(actual, expected)

    def test_get_geo_invalid_api_key(self):
        actual = get_geo('134.201.250.155', 'invalid')
        expected = {'success': False,
                    'error': {'code': 101,
                    'type': 'invalid_access_key',
                    'info': 'You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]'}}
        self.assertEquals(actual, expected)


=======
import unittest

from geo.utilities import get_geo


class TestGetGeo(unittest.TestCase):

    def test_get_geo_valid_ip(self):
        actual = get_geo('134.201.250.155')
        expected = 'Geolocation added!'
        self.assertEquals(actual, expected)

    def test_get_geo_invalid_ip(self):
        actual = get_geo('12')
        expected = { "Error" : "Invalid IP address" }
        self.assertEquals(actual, expected)


>>>>>>> ee8166a3b8bf4aaa4a9a9f9975f0fd942f57854e
