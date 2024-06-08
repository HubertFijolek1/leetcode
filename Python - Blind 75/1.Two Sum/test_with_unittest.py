import unittest
from brute_force import two_sum_brute_force
from optimized_solution import two_sum_hash_table

class TestTwoSumMethods(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(two_sum_brute_force([2, 7, 11, 15], 9), [0, 1])
        self.assertIsNone(two_sum_brute_force([3, 2], 7))

    def test_hash_table(self):
        self.assertEqual(two_sum_hash_table([2, 7, 11, 15], 9), [0, 1])
        self.assertIsNone(two_sum_hash_table([3, 2], 7))

if __name__ == '__main__':
    unittest.main()
