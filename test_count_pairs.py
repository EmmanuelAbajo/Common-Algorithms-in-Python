import unittest
from count_pairs import count_pairs

class CountPairsTest(unittest.TestCase):
    def test_count_pairs_1(self):
        self.assertEqual(count_pairs([1,5,7,-1], 6), 2, 'Expected is 2')

    def test_count_pairs_2(self):
        self.assertEqual(count_pairs([1,5,7,-1,5], 6), 3, 'Expected is 3')

    def test_count_pairs_3(self):
        self.assertEqual(count_pairs([1,1,1,1], 2), 6, 'Expected is 6')  

    def test_count_pairs_4(self):
        self.assertEqual(count_pairs([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11), 9, 'Expected is 9')            

if __name__ == '__main__':
    unittest.main()        
