def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{seed_type} s    ds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_type} seds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type} seds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
