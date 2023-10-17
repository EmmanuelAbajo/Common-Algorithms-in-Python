import unittest
from coin_change import get_coin_change_ways_unique

class CoinChangeTest(unittest.TestCase):
    def test_coin_change_1(self):
        self.assertEqual(get_coin_change_ways_unique([8,3,1,2], 3), 3, 'Expected is 3')

    def test_coin_change_2(self):
        self.assertEqual(get_coin_change_ways_unique([1,2,3], 4), 4, 'Expected is 4')

    def test_coin_change_3(self):
        self.assertEqual(get_coin_change_ways_unique([2,3,5,6], 10), 5, 'Expected is 5')

    def test_coin_change_4(self):
        self.assertEqual(get_coin_change_ways_unique([2], 3), 0, 'Expected is 0')

    def test_coin_change_4(self):
        self.assertEqual(get_coin_change_ways_unique([1,2,5], 5), 4, 'Expected is 4')    
             

if __name__ == '__main__':
    unittest.main()  