import unittest
from store import discounts

class test_case(unittest.TestCase):
    def test_under_10(self):
        self.assertLess(discounts.calculate_order(9, 5, 10), 10)
        self.assertLess(discounts.calculate_order(9, 5, 15), 10)
        self.assertLess(discounts.calculate_order(9, 5, 20), 10)
        self.assertLess(discounts.calculate_order(9, 10, 10), 10)

    def test_10_lessthan_30(self):
        self.assertLess(discounts.calculate_order(25, 5, 10), 10)
        self.assertLess(discounts.calculate_order(25, 5, 15), 10)
        self.assertLess(discounts.calculate_order(25, 5, 20), 10)
        self.assertLess(discounts.calculate_order(25, 10, 10), 10)
        self.assertLess(discounts.calculate_order(25, 10, 20), 10)
        self.assertLess(discounts.calculate_order(24, 20, 10), 10)

    def test_10_lessthan_50(self):
        self.assertLess(discounts.calculate_order(49, 5, 10), 10)
        self.assertLess(discounts.calculate_order(49, 10, 15), 10)
        self.assertLess(discounts.calculate_order(49, 10, 20), 10)
        self.assertLess(discounts.calculate_order(49, 10, 25), 10)
        self.assertLess(discounts.calculate_order(49, 15, 10), 10)
        self.assertLess(discounts.calculate_order(49, 15, 15), 10)
        self.assertLess(discounts.calculate_order(49, 15, 25), 10)
        self.assertLess(discounts.calculate_order(49, 25, 10), 10)
        self.assertLess(discounts.calculate_order(49, 25, 15), 10)
        self.assertLess(discounts.calculate_order(49, 25, 25), 10)
        self.assertLess(discounts.calculate_order(49, 10, 25), 10)

    def test_50_and_above(self):
        self.assertGreaterEqual(discounts.calculate_order(85, 5, 10), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 10), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 15), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 20), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 10, 25), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 5), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 10), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 15), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 15, 25), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 5), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 10), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 15), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 20), 100)
        self.assertGreaterEqual(discounts.calculate_order(85, 25, 25), 100)


if __name__ == "__main__":
    unittest.main()
