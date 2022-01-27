import unittest

from deepcomparer import deep_compare


class TestCompareListIgnoringOrderButSorted(unittest.TestCase):
    def test_empty_list(self):
        """
        Test empty list
        """
        data1: list = []
        data2: list = []
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_different_size_lists(self):
        """
        Test different size lists
        """
        data1: list = [1]
        data2: list = []
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists_with_different_values(self):
        """
        Test same size lists with different values
        """
        data1: list = [1]
        data2: list = [2]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists(self):
        """
        Test same size lists with different values
        """
        data1: list = [1]
        data2: list = [1]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_empty_list_inside_list(self):
        """
        Test empty list inside list
        """
        data1: list = [[]]
        data2: list = [[]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_different_size_lists_inside_list(self):
        """
        Test different size lists inside list
        """
        data1: list = [[1]]
        data2: list = [[]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists_with_different_values_inside_list(self):
        """
        Test same size lists with different values inside list
        """
        data1: list = [[1]]
        data2: list = [[2]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists_inside_list(self):
        """
        Test same size lists with different values inside list
        """
        data1: list = [[3]]
        data2: list = [[3]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_same_size_lists_with_different_values_with_many_values(self):
        """
        Test same size lists with different values
        """
        data1: list = [1, 2]
        data2: list = [2]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists_with_many_values(self):
        """
        Test same size lists with different values
        """
        data1: list = [1, 2]
        data2: list = [1, 2]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_empty_list_inside_list_with_many_values(self):
        """
        Test empty list inside list
        """
        data1: list = [[3], [1, 2]]
        data2: list = [[3], [1, 2]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)

    def test_different_size_lists_inside_list_with_many_values(self):
        """
        Test different size lists inside list
        """
        data1: list = [[1], [1, 2, 3]]
        data2: list = [[], [1, 2, 3]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists_with_different_values_inside_list_with_many_values(self):
        """
        Test same size lists with different values inside list
        """
        data1: list = [[1], [2]]
        data2: list = [[2], [3]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertFalse(result)

    def test_same_size_lists_inside_list_with_many_values(self):
        """
        Test same size lists with different values inside list
        """
        data1: list = [[3], [4, 5, 6]]
        data2: list = [[3], [4, 5, 6]]
        result = deep_compare(data1, data2, ignore_order=True)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
