import unittest


from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """测试city_funtions.py"""

    def test_city_country(self):
        """传入简单的城市和国家测试吗"""
        sc = city_country('santiago', 'chile', '600')
        self.assertEqual(sc, 'Santiago Chile-population 600')


if __name__ == '__main__':
    unittest.main()