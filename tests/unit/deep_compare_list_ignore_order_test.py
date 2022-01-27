import unittest

from deepcomparer import deep_compare


class TestCompareListIgnoringOrder(unittest.TestCase):

    def test_same_size_lists_with_many_values(self):
        """
        Test same size lists with different values
        """
        data1: list = [2, 1]
        data2: list = [1, 2]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_empty_list_inside_list_with_many_values(self):
        """
        Test empty list inside list
        """
        data1: list = [[1, 2], [3]]
        data2: list = [[3], [2, 1]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_different_size_lists_inside_list_with_many_values(self):
        """
        Test different size lists inside list
        """
        data1: list = [[1], [1, 2, 3]]
        data2: list = [[], [2, 1, 3]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists_inside_list_with_many_values(self):
        """
        Test same size lists with different values inside list
        """
        data1: list = [[4, 6, 5], [3]]
        data2: list = [[3], [4, 5, 6]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
