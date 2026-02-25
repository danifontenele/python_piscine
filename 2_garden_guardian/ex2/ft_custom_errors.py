class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def get_plant_error():
    raise PlantError("The tomato plant is wilting!")


def get_water_error():
    raise WaterError("Not enought water in the tank!")


def test_error_types() -> None:
    print("\nTesting PlantError...")
    try:
        get_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        get_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        get_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        get_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_error_types()
    print("All custom error types work correctly!")
