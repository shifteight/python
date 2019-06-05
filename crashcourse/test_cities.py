import unittest
from city_functions import get_city_info

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        
        city_info = get_city_info('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')
    
    def test_city_country_population(self):
        
        city_info = get_city_info(
            'santiago', 'chile', 500000
        )
        self.assertEqual(city_info, 'Santiago, Chile - population 500000')

unittest.main()