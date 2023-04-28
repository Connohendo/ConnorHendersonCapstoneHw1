from dataclasses import dataclass

@dataclass
class Item:
    name: str
    item_type: str
    price: float

# Example usage:
items = [
    Item("Milk", "Wic Eligible food", 4.75),
    Item("Bread", "Wic Eligible food", 5.50),
    Item("Fur Scarf", "Clothing", 75.00),
    Item("T-shirt", "Clothing", 12.00),
    Item("Pants", "Clothing", 40.00),
    Item("Fur Coat", "Clothing", 200.00),
    Item("Laptop", "Everything else", 1200.00),
    Item("Smartphone", "Everything else", 900.00)
]