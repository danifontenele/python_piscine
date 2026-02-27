import sys


def dictionary_factory() -> dict:
    ac = len(sys.argv)
    arg = sys.argv
    inventory = {}
    i = 1
    while i < ac:
        name, quantity = arg[i].split(":")
        inventory[name] = int(quantity)
        i += 1
    return inventory


def inventory_system_analysis(inventory: dict, total: int) -> None:
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")


def show_current_inventory(inventory: dict, total: int) -> None:
    print("=== Current Inventory ===")

    for name, quantity in inventory.items():
        percentage = quantity / total * 100
        print(f"{name}: {quantity} units ({percentage:.1f}%)")


def show_inventory_statistics(inventory: dict) -> None:
    biggest_item = None
    biggest_value = -1
    smallest_item = None
    smallest_value = float("inf")

    for name, quantity in inventory.items():
        if quantity > biggest_value:
            biggest_item = name
            biggest_value = quantity
        if quantity < smallest_value:
            smallest_item = name
            smallest_value = quantity

    print("=== Inventory Statistics ===")
    print(f"Most abundant: {biggest_item} ({biggest_value})")
    print(f"Least abundant: {smallest_item} ({smallest_value})")


def show_item_categories():
    print("=== Item Categories ===")

def show_management_suggestions(inventory: dict) -> None:
    print("=== Management Suggestions ===")


def show_dictionary_properties(inventory: dict) -> None:
    print("=== Dictionary Properties Demo ===")
    items = ", ".join(inventory)
    values = ", ".join(str(v) for v in inventory.values())
    print(f"Dictionary keys: {items}")
    print(f"Dictionary values: {values}")


def main() -> None:
    inventory = dictionary_factory()
    total = sum(inventory.values())
    if total == 0:
        return
    inventory_system_analysis(inventory, total)
    print("")
    show_current_inventory(inventory, total)
    print("")
    show_inventory_statistics(inventory)
    print("")
    show_item_categories()
    print("")
    show_management_suggestions(inventory)
    print("")
    show_dictionary_properties(inventory)


if __name__ == "__main__":
    main()
