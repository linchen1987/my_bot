import unittest
from crypto import format_price


class TestFormatPrice(unittest.TestCase):
    def test_price_greater_than_or_equal_to_one(self):
        self.assertEqual(format_price(1.01), "1.01")
        self.assertEqual(format_price(10.22), "10.22")
        self.assertEqual(format_price(100.456), "100.46")
        self.assertEqual(format_price(999.999), "1,000.00")
        self.assertEqual(format_price(1.0), "1.00")

    def test_price_less_than_one(self):
        self.assertEqual(format_price(0.23), "0.23")
        self.assertEqual(format_price(0.12), "0.12")
        self.assertEqual(format_price(0.082), "0.082")
        self.assertEqual(format_price(0.021), "0.021")
        self.assertEqual(format_price(0.001), "0.0010")
        self.assertEqual(format_price(0.000001), "0.0000010")
        self.assertEqual(format_price(0.5), "0.50")
        self.assertEqual(format_price(0.025), "0.025")
        self.assertEqual(format_price(0.00001), "0.000010")
        self.assertEqual(format_price(0.0000001), "0.0000001")


if __name__ == "__main__":
    unittest.main()
