import unittest
from store import discounts

class test_case(unittest.TestCase):
    def test_under_10(self):
        self.assertLess(discounts.calculate_order(9, 5, 10), 10)
        self.assertLess(discounts.calculate_order(9, 5, 15), 10)
        self.assertLess(discounts.calculate_order(9, 5, 20), 10)
        self.assertLess(discounts.calculate_order(9, 10, 10), 10)

    def test_10_lessthan_30(self):
        self.assertLess(discounts.calculate_order(25, 5, 10), 30)
        self.assertLess(discounts.calculate_order(25, 5, 15), 30)
        self.assertLess(discounts.calculate_order(25, 5, 20), 30)
        self.assertLess(discounts.calculate_order(25, 10, 10), 30)
        self.assertLess(discounts.calculate_order(25, 10, 20), 30)
        self.assertLess(discounts.calculate_order(24, 20, 10), 30)

    def test_10_lessthan_50(self):
        self.assertLess(discounts.calculate_order(40, 5, 10), 50)
        self.assertLess(discounts.calculate_order(45, 10, 15), 50)
        self.assertLess(discounts.calculate_order(45, 10, 20), 50)
        self.assertLess(discounts.calculate_order(45, 10, 25), 50)
        self.assertLess(discounts.calculate_order(45, 15, 10), 50)
        self.assertLess(discounts.calculate_order(45, 15, 15), 50)
        self.assertLess(discounts.calculate_order(45, 15, 25), 50)
        self.assertLess(discounts.calculate_order(45, 25, 10), 50)
        self.assertLess(discounts.calculate_order(45, 25, 15), 50)
        self.assertLess(discounts.calculate_order(45, 25, 25), 50)
        self.assertLess(discounts.calculate_order(45, 10, 25), 50)

    def test_50_and_above(self):
        self.assertGreaterEqual(discounts.calculate_order(85, 5, 10), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 10), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 15), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 20), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 25), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 5), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 10), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 15), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 25), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 5), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 10), 50)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 15), 50)
        self.assertGreaterEqual(discounts.calculate_order(100, 25, 20), 50)
        self.assertGreaterEqual(discounts.calculate_order(100, 25, 25), 50)


if __name__ == "__main__":
    unittest.main()
