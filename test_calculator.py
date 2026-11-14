import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertNotEqual(add(3, 4), 5)
        self.assertEqual(add(-1, -3), -4)
        self.assertEqual(add(-1, 2), 1)
    def test_subtract(self):
        self.assertEqual(sub(1, 2), -1)
        self.assertEqual(sub(3, -1), 4)
        self.assertNotEqual(sub(1, 2), 3)
        self.assertEqual(sub(1, 0), 1)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)
            div(0, 2.1)
            div(0, -1)
            div(0, 0)
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 10), 1)
        self.assertAlmostEqual(logarithm(1, 2), 0)
        self.assertAlmostEqual(logarithm(0.1, 10), -1)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(2, -10)
            logarithm(2, -1)
        with self.assertRaises(ZeroDivisionError):
            logarithm(2, 1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()