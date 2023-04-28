import unittest
from checkout import Item, calculate_total

class TestCalculation(unittest.TestCase):

    def setUp(self):
        self.items = [
            Item("Milk", "Wic Eligible food", 4.75),
            Item("Pants", "Clothing", 40.00),
            Item("Fur Scarf", "Clothing", 75.00),
            Item("Laptop", "Everything else", 1200.00)
        ]

    def test_normal_calulation(self):
        self.assertAlmostEqual(calculate_total("NJ", self.items), 1403.90, places=2)
        self.assertAlmostEqual(calculate_total("DE", self.items), 1319.75, places=2)
        self.assertAlmostEqual(calculate_total("PA", self.items), 1396.25, places=2)

    def test_empty_item_type(self):
        items = [
            Item("Milk", "", 3.00),
            Item("Jeans", "", 40.00)
        ]

        with self.assertRaises(ValueError, msg="Item type cannot be empty."):
            calculate_total("NJ", items)

    def test_empty_cart(self):
        items = []

        with self.assertRaises(ValueError, msg="No items in cart. Please add at least one item."):
            calculate_total("NJ", items)

    def test_zero_total(self):
        items = [
            Item("Milk", "Wic Eligible food", 0.00),
            Item("Bread", "Wic Eligible food", 0.00)
        ]

        with self.assertRaises(ValueError, msg="Total cannot be zero. Please add a taxable item to the cart."):
            calculate_total("DE", items)

    def test_invalid_state(self):
        with self.assertRaises(ValueError, msg="Invalid state. Supported states are 'NJ', 'DE', and 'PA'."):
            calculate_total("NY", self.items)

if __name__ == '__main__':
    unittest.main()
