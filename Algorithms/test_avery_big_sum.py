import unittest
from test_avery_big_sum import a_very_big_sum

class TestAVeryBigSum(unittest.TestCase):
    """
    This class contains unit tests for the `aVeryBigSum` function.
    """

    def test_sample_input(self):
        """
        Test case for the `aVeryBigSum` function with a sample input.
        """
        ar = [1000001, 1000002, 1000003, 1000004, 1000005]
        self.assertEqual(a_very_big_sum(ar), 5000015)

    def test_empty_arr(self):
        """
        Test case for the `aVeryBigSum` function with an empty array.
        """
        self.assertEqual(a_very_big_sum([]), 0)
    
    def test_single_element(self):
        """
        Test case for the `aVeryBigSum` function with a single element array.
        """
        self.assertEqual(a_very_big_sum([1000000]), 1000000)

if __name__ == '__main__':
    unittest.main()
