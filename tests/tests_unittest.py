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


