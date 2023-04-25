import unittest
from unittest.mock import MagicMock, patch
from app import app
from utils import helpers


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('utils.service.requests.get')
    def test_average_exchange_rate(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: {'rates': [{'mid': 3.5}]})
        response = self.client.get(
            '/average_exchange_rate?currency_code=USD&date=2023-04-24')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'rate': 3.5})

    @patch('utils.service.requests.get')
    def test_max_min_average(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {
                                          'rates': [{'mid': 3.5}, {'mid': 3.6}, {'mid': 3.7}]})
        response = self.client.get(
            '/max_min_average?currency_code=USD&count=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'min_rate': 3.5, 'max_rate': 3.7})

    @patch('utils.service.requests.get')
    def test_major_difference(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {
                                          'rates': [{'ask': 4.0, 'bid': 3.0}, {'ask': 4.2, 'bid': 3.2}]})
        response = self.client.get(
            '/major_difference?currency_code=USD&count=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'major_difference': 1.0})

    def test_validate_date(self):
        with self.assertRaises(ValueError):
            helpers.validate_date('')
        with self.assertRaises(ValueError):
            helpers.validate_date('2023-04-23')  # a Sunday
        with self.assertRaises(ValueError):
            helpers.validate_date('2023-05-01')  # a holiday

    def test_validate_currency(self):
        with self.assertRaises(ValueError):
            helpers.validate_currency('')
        with self.assertRaises(ValueError):
            helpers.validate_currency('USD1')  # invalid format

    def test_validate_count(self):
        with self.assertRaises(ValueError):
            helpers.validate_count(0)
        with self.assertRaises(ValueError):
            helpers.validate_count(256)  # greater than 255
        with self.assertRaises(ValueError):
            helpers.validate_count('one')  # not an integer
