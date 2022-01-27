import unittest

from deepcomparer import deep_compare


class TestCompareDict(unittest.TestCase):
    def test_empty_dict(self):
        """
        Test empty dict
        """
        data1: dict = {}
        data2: dict = {}
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_different_size_dicts(self):
        """
        Test different size dicts
        """
        data1: dict = {'a': 1}
        data2: dict = {}
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_dicts_with_different_keys(self):
        """
        Test empty same size dicts with different keys
        """
        data1: dict = {'a': 1}
        data2: dict = {'b': 1}
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_dicts_with_different_values(self):
        """
        Test same size dicts with different values
        """
        data1: dict = {'a': 1}
        data2: dict = {'a': 2}
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_dicts(self):
        """
        Test same size dicts with different values
        """
        data1: dict = {'a': 1}
        data2: dict = {'a': 1}
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_empty_dict_inside_dict(self):
        """
        Test empty dict inside dict
        """
        data1: dict = {'a': {}}
        data2: dict = {'a': {}}
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_different_size_dicts_inside_dict(self):
        """
        Test different size dicts inside dict
        """
        data1: dict = {'b': {'a': 1}}
        data2: dict = {'b': {}}
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_dicts_with_different_keys_inside_dict(self):
        """
        Test empty same size dicts with different keys inside dict
        """
        data1: dict = {'a': {'a': 1}}
        data2: dict = {'a': {'b': 1}}
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_dicts_with_different_values_inside_dict(self):
        """
        Test same size dicts with different values inside dict
        """
        data1: dict = {'a': {'a': 1}}
        data2: dict = {'a': {'a': 2}}
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_same_size_dicts_inside_dict(self):
        """
        Test same size dicts with different values inside dict
        """
        data1: dict = {'z': {'a': 1}}
        data2: dict = {'z': {'a': 1}}
        result = deep_compare(data1, data2)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
