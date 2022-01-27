import unittest

from deepcomparer import deep_compare


class TestCompareTuple(unittest.TestCase):
    def test_empty_tuple(self):
        """
        Test empty tuple
        """
        data1: tuple = ()
        data2: tuple = ()
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_empty_tuple_inside_tuple(self):
        """
        Test empty tuple inside tuple
        """
        data1: tuple = (())
        data2: tuple = (())
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_same_size_tuples_with_different_values_with_many_values(self):
        """
        Test same size tuples with different values
        """
        data1: tuple = (1, 2)
        data2: tuple = (2, 2, 3)
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_tuples_with_many_values(self):
        """
        Test same size tuples with different values
        """
        data1: tuple = (1, 2)
        data2: tuple = (1, 2)
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_empty_tuple_inside_tuple_with_many_values(self):
        """
        Test empty tuple inside tuple
        """
        data1: tuple = ((3, 2), (1, 2))
        data2: tuple = ((3, 2), (1, 2))
        result = deep_compare(data1, data2)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
