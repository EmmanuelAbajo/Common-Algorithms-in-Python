import unittest
from min_coins import find_min_coins, find_minimum_coins

class MinCoinsTest(unittest.TestCase):
    def test_find_min_coins_1(self):
        self.assertEqual(find_min_coins([25,10,5], 30), 2, 'Expected is 2')

    def test_find_min_coins_2(self):
        self.assertEqual(find_min_coins([9, 6, 5, 1], 11), 2, 'Expected is 2')

    def test_find_min_coins_3(self):
        self.assertEqual(find_min_coins([1,3,6], 11), 4, 'Expected is 4')

    def test_find_min_coins_4(self):
        self.assertEqual(find_min_coins([1,4,5], 150), 30, 'Expected is 30')

    def test_find_minimum_coins_1(self):
        self.assertEqual(find_minimum_coins([25,10,5], 30), 2, 'Expected is 2')

    def test_find_minimum_coins_2(self):
        self.assertEqual(find_minimum_coins([9, 6, 5, 1], 11), 2, 'Expected is 2')

    def test_find_minimum_coins_3(self):
        self.assertEqual(find_minimum_coins([1,3,6], 11), 4, 'Expected is 4')

    def test_find_minimum_coins_4(self):
        self.assertEqual(find_minimum_coins([1,4,5], 150), 30, 'Expected is 30')       

if __name__ == '__main__':
    unittest.main()          