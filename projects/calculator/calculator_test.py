import unittest
from projects.calculator.calculator import Calculator

class TestSum(unittest.TestCase):
    def test_sum(self):
        obj = Calculator()
        self.assertEqual(obj.add(1,2),3)
        self.assertEqual(obj.add(2,3),5)
        #to fail any test just change the values so that sum is not equal


if __name__ == '__main__':
    unittest.main()