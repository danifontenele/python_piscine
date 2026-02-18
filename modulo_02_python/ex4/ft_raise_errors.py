class PlantNameError(Exception):
    pass


class WaterError(Exception):
    pass


class SunlightError(Exception):
    pass

def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None:
        raise PlantNameError("Plant name cannot be empty!")

    if water_level > 10:
        raise WaterError(f"Water level {water_level} is too high (max 10)")

    elif water_level < 1:
        raise WaterError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours > 12:
        raise SunlightError(f"Sunlight hours {sunlight_hours} "
                                f"is too high (max 12)")
    elif sunlight_hours < 2:
        raise SunlightError(f"Sunlight hours {sunlight_hours} "
                                f"is too low (min 2)")
    print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 7, 5)
    except (PlantNameError, WaterError, SunlightError) as e:
        print(f"Error: {e}\n")
    print("Testing empty plants name...")
    try:
        check_plant_health(None, 15, 5)
    except (PlantNameError, WaterError, SunlightError) as e:
        print(f"Error: {e}\n")
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except (PlantNameError, WaterError, SunlightError) as e:
        print(f"Error: {e}\n")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 7, 0)
    except (PlantNameError, WaterError, SunlightError) as e:
        print(f"Error: {e}\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
