import unittest
from even_odd import even_or_odd
from bonus import calcbonus


class MyTestCase(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual("the number 13 is odd", even_or_odd(13))
        self.assertEqual("the number 24 is even", even_or_odd(24))

    # In the space below, write a test function for bonus. Make sure to import the appropriate information
    # at the top of this file. Make sure to write three test cases.
    def test_bonus(self):
        # when you are ready to write your tests, go ahead and delete pass
        self.assertEqual("105.0", calcbonus(10, 100))
        self.assertEqual("105.0", calcbonus(5, 100))
        self.assertEqual("You are not eligible for a bonus.", calcbonus(1, 100))

if __name__ == '__main__':
    unittest.main()
