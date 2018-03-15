import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPythonLoops(unittest.TestCase):
    def test_city_indices_list(self):
        self.assertEqual(city_indices, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_names_and_ranks_list(self):
        self.assertEqual(names_and_ranks[0], '1. Solta')
        self.assertEqual(names_and_ranks[-1], '12. Pyeongchang')

    def test_city_indices_list(self):
        self.assertEqual(city_indices, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_city_populations(self):
        self.assertEqual(city_populations, [1700, 84554, 13591863, 287651, 32237, 928850, 559277, 60000, 0, 4000, 630, 2581000])

    def test_city_populations(self):
        self.assertEqual(city_areas, [59, 68, 4758, 3750, 33, 200, 491, 8300, 672, 27, 2731571, 3194])
