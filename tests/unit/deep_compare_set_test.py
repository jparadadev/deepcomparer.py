import unittest

from deepcomparer import deep_compare


class TestCompareSet(unittest.TestCase):
    def test_empty_set(self):
        """
        Test empty set
        """
        data1: set = set()
        data2: set = set()
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_different_size_sets(self):
        """
        Test different size sets
        """
        data1: set = {1}
        data2: set = set()
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_sets_with_different_values(self):
        """
        Test same size sets with different values
        """
        data1: set = {1}
        data2: set = {2}
        result = deep_compare(data1, data2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
