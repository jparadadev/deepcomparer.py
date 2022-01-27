import unittest

from deepcomparer import deep_compare


class TestCompareByPlain(unittest.TestCase):
    def test_with_basic_equal_numbers(self):
        """
        Test basic number
        """
        data1: int = 39
        data2: int = 39
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_with_basic_different_numbers(self):
        """
        Test basic number
        """
        data1: int = 39
        data2: int = 2
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_with_equal_floats(self):
        """
        Test float
        """
        data1: float = 39.0
        data2: float = 39.0
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_with_different_floats(self):
        """
        Test float
        """
        data1: float = 4.0
        data2: float = 39.0
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_with_equal_strings(self):
        """
        Test string
        """
        data1: str = 'fox'
        data2: str = 'fox'
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_with_different_strings(self):
        """
        Test string
        """
        data1: str = 'cat'
        data2: str = 'dog'
        result = deep_compare(data1, data2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
