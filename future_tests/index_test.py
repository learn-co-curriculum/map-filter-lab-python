import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPythonMapFilter(unittest.TestCase):
    def test_names(self):
        self.assertItemsEqual(names, ['Fork & Fig', 'Salt And Board', 'Frontier Restaurant', 'Nexus Brewery', "Devon's Pop Smoke", 'Cocina Azul', 'Philly Steaks', 'Stripes Biscuit'])

    def test_review_counts(self):
        self.assertItemsEqual(review_counts, [610, 11, 1373, 680, 54, 647, 25, 20])

    def test_total_reviews(self):
        self.assertEqual(total_reviews, 3420)

    def test_format_restaurants_func(self):
        self.assertItemsEqual(format_restaurants(restaurants), [{'name': 'Fork & Fig', 'price': 2, 'is_closed': False, 'review_count': 610},
        {'name': 'Salt And Board', 'price': 2, 'is_closed': False, 'review_count': 11},
        {'name': 'Frontier Restaurant', 'price': 1, 'is_closed': False, 'review_count': 1373},
        {'name': 'Nexus Brewery', 'price': 2, 'is_closed': False, 'review_count': 680},
        {'name': "Devon's Pop Smoke", 'price': 2, 'is_closed': False, 'review_count': 54},
        {'name': 'Cocina Azul', 'price': 2, 'is_closed': True, 'review_count': 647},
        {'name': 'Philly Steaks', 'price': 2, 'is_closed': False, 'review_count': 25},
        {'name': 'Stripes Biscuit', 'price': 2, 'is_closed': True, 'review_count': 20}])

    def test_open_restaurants_func(self):
        self.assertItemsEqual(open_restaurants(restaurants), [{'name': 'Fork & Fig', 'price': 2, 'is_closed': False, 'review_count': 610},
        {'name': 'Salt And Board', 'price': 2, 'is_closed': False, 'review_count': 11},
        {'name': 'Frontier Restaurant', 'price': 1, 'is_closed': False, 'review_count': 1373},
        {'name': 'Nexus Brewery', 'price': 2, 'is_closed': False, 'review_count': 680},
        {'name': "Devon's Pop Smoke", 'price': 2, 'is_closed': False, 'review_count': 54},
        {'name': 'Philly Steaks', 'price': 2, 'is_closed': False, 'review_count': 25}])

    def test_cheapest_restaurants_func(self):
        self.assertItemsEqual(cheapest_restaurants(restaurants), [{'name': 'Frontier Restaurant', 'price': 1, 'is_closed': False, 'review_count': 1373}])

    def test_sufficiently_reviewed_restaurants_func(self):
        self.assertItemsEqual(sufficiently_reviewed_restaurants(restaurants), [{'name': 'Fork & Fig', 'price': 2, 'is_closed': False, 'review_count': 610},
        {'name': 'Frontier Restaurant', 'price': 1, 'is_closed': False, 'review_count': 1373},
        {'name': 'Nexus Brewery', 'price': 2, 'is_closed': False, 'review_count': 680},
        {'name': 'Cocina Azul', 'price': 2, 'is_closed': True, 'review_count': 647}])
