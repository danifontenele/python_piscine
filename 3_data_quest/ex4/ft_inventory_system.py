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

def show_current_inventory(inventory: dict) -> None:
    sword = inventory.get("sword")
    potion = inventory.get("potion")
    shield = inventory.get("shield")
    armor = inventory.get("armor")
    helmet = inventory.get("helmet")
    total = sword + potion + shield + armor + helmet
    print ("=== Current Inventory ===")
    print(f"sword: {sword} units ({sword / total * 100:.1f}%)")
    print(f"potion: {potion} units ({potion / total * 100:.1f}%)")
    print(f"shield: {shield} units ({shield / total * 100:.1f}%)")
    print(f"armor: {armor} units ({armor / total * 100:.1f}%)")
    print(f"helmet: {helmet} units ({helmet / total * 100:.1f}%)")

def show_inventory_statistics(inventory: dict) -> None:
    pass
	

def main() -> None:
    inventory = dictionary_factory()
    show_current_inventory(inventory)
    inventory_statistics(inventory)


if __name__ == "__main__":
    main()
