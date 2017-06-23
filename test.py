import unittest
from bin_generator import BinGenerator

class TestHelperMethods(unittest.TestCase):

    def test_is_int(self):
        self.assertTrue(self.isInt(2))
        self.assertTrue(self.isInt(-2))
        self.assertFalse(self.isInt('a'))
        self.assertFalse(self.isInt('3d'))
        self.assertFalse(self.isInt('a9'))

    def test_is_special_line(self):
        self.assertTrue(self.isSpecialLine("Ref   start   stop"))
        self.assertFalse(self.isSpecialLine("chr1   20348   58392"))


if __name__ == '__main__':
    unittest.main()
