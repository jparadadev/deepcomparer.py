import unittest

from deepcomparer import deep_compare


class Cat:
    def __init__(self, a):
        self.a = a


class Dog:
    def __init__(self, a):
        self.a = a


class TestCompareDict(unittest.TestCase):

    def test_equal_classes(self):
        """
        Test equal classes
        """
        data1 = Cat(1)
        data2 = Cat(1)
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_same_classes_different_values(self):
        """
        Test equal classes with different values
        """
        data1 = Cat(1)
        data2 = Cat(2)
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_different_classes_same_values(self):
        """
        Test different classes with same values
        """
        data1 = Cat(1)
        data2 = Dog(1)
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_equals_embeded_classes(self):
        data1 = Cat(Dog(2))
        data2 = Cat(Dog(2))
        result = deep_compare(data1, data2)
        self.assertTrue(result)

    def test_different_embeded_classes(self):
        data1 = Cat(Dog(2))
        data2 = Cat(Dog(1))
        result = deep_compare(data1, data2)
        self.assertFalse(result)

    def test_different_typed_embeded_classes(self):
        data1 = Dog(Cat(1))
        data2 = Cat(Dog(1))
        result = deep_compare(data1, data2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
