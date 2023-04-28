from dataclasses import dataclass
from typing import List
from records import items

@dataclass
class Item:
    name: str
    item_type: str
    price: float

def is_fur_clothing(item: Item) -> bool:
    return "clothing" in item.item_type.lower() and "fur" in item.name.lower()

def is_tax_exempt(item: Item, state: str) -> bool:
    if "wic eligible food" in item.item_type.lower():
        return True
    if "clothing" in item.item_type.lower() and state in ["PA", "NJ"] and not is_fur_clothing(item):
        return True
    return False

def apply_sales_tax(item: Item, state: str) -> float:
    if is_tax_exempt(item, state):
        return item.price
    elif state == "NJ":
        return item.price * 1.066
    elif state == "PA":
        return item.price * 1.06
    else:
        return item.price

def calculate_total(state: str, items: List[Item]) -> float:
    if state not in ["NJ", "DE", "PA"]:
        raise ValueError("Invalid state. Supported states are 'NJ', 'DE', and 'PA'.")
    if not items:
        raise ValueError("No items in cart. Please add at least one item.")
    for item in items:
        if not item.item_type:
            raise ValueError("Item type cannot be empty.")
    total = sum(apply_sales_tax(item, state) for item in items)
    if total == 0:
        raise ValueError("Total cannot be zero. Please add a taxable item to the cart.")
    return total

def main() -> None:
    print("Please select your state:")
    print("1. Delaware (DE)")
    print("2. New Jersey (NJ)")
    print("3. Pennsylvania (PA)")

    state_list = {
        "1": "DE",
        "2": "NJ",
        "3": "PA"
    }

    while True:
        user_state_choice = input("Please enter the number corresponding to your state: ")
        if user_state_choice in state_list:
            selected_state = state_list[user_state_choice]
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")    
    try:
        total_cost = calculate_total(selected_state, items)
        print(f"The total to charge a customer at checkout: ${total_cost:.2f}")
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
