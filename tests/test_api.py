import unittest

from app import app
app.testing = True


class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_func_name(self):
        request = self.app.get('/address?house_number=100&street=Gold st&borough_code=1')
        response = request.json
        self.assertFalse(response['error'])
        self.assertIsNotNone(response['result']['First Borough Name'])
        self.assertIsNotNone(response['result']['House Number - Display Format'])
        self.assertIsNotNone(response['result']['First Street Name Normalized'])

    def test_func_code(self):
        request = self.app.get('/1b?house_number=100&street=Gold st&borough_code=1')
        response = request.json
        self.assertFalse(response['error'])
        self.assertIsNotNone(response['result']['First Borough Name'])
        self.assertIsNotNone(response['result']['House Number - Display Format'])
        self.assertIsNotNone(response['result']['First Street Name Normalized'])

    def test_attr_error(self):
        fake_func = '0'
        request = self.app.get('/{}'.format(fake_func))
        response = request.json
        self.assertTrue(response['error'])
        self.assertEqual(response['result']["Message"],  "Unknown Geosupport function '{}'.".format(fake_func))

    def test_geo_error(self):
        request = self.app.get('/address')
        response = request.json
        self.assertTrue(response['error'])
        self.assertEqual(response['result']["Message"],  "NO INPUT DATA RECEIVED")