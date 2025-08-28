import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1, -1), 0)
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        # Add more assertions to thoroughly test the subtract method.
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        self.assertEqual(self.calc.subtract(1000000, 2000000), -1000000)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Add more assertions to thoroughly test the multiply method.
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(1, -1), -1)
        self.assertEqual(self.calc.multiply(1000000, 2000000), 2000000000000)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(2, 3), 2/3)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        # Add more assertions to thoroughly test the divide method.
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(1, 0), None)
         # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

