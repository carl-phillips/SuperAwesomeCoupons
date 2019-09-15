import unittest
from store import discounts

class test_case(unittest.TestCase):
    def test_under_10(self):
        self.assertLess(10, discounts.calculate_order(9, 5, 10))
        self.assertLess(10, discounts.calculate_order(9, 5, 15))
        self.assertLess(10, discounts.calculate_order(9, 5, 20))
        self.assertLess(10, discounts.calculate_order(9, 10, 10))

if __name__ == "__main__":
    unittest.main()
