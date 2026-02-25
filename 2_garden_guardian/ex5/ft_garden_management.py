class GardenError(Exception):
    pass


class PlantNameError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun
        if name is None or name == "":
            raise PlantNameError("Plant name cannot be empty!")


class GardenManager:
    # Every created manager has your own plant_list
    def __init__(self, manager: str):
        self.manager = manager
        self.plant_list = []

    # Add plant function: if has a name, add that plant
    def add_plant(self, name: str, water_level: int, sunlight: int) -> None:
        try:
            self.plant_list.append(Plant(name, water_level, sunlight))
            print(f"Added {name} successfully")
        except PlantNameError as e:
            print(f"Error adding plant: {e}")

    # Watering function: add water level
    def watering(self) -> None:
        print("Opening watering system")
        for plant in self.plant_list:
            plant.water += 1
            if plant.water > 10:
                raise WaterError("Water level is too high (max 10)")
            elif plant.water < 1:
                raise WaterError("Not enough water in the tank")
            print(f"Watering {plant.name} - success")

    # Check_health function: check water level and sunlight time
    def check_health(self) -> None:
        for plant in self.plant_list:
            if plant.water > 10:
                print(f"Error checking {plant.name}: water level is "
                      "too high (max 10)")
            elif plant.water < 1:
                print(f"Error checking {plant.name}: water level is "
                      "too low (min 1)")
            elif plant.sun > 12:
                print(f"Error checking {plant.name}: sunlight level is "
                      "too high (max 12)")
            elif plant.sun < 2:
                print(f"Error checking {plant.name}: sunlight level is "
                      "too low (min 2)")
            else:
                print(f"{plant.name}: healthy(water: {plant.water}, "
                      f"sun: {plant.sun})")


def test_garden_management():
    manager = GardenManager("Manager")
    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    manager.add_plant("Sunflower", 9, 12)
    manager.add_plant("Tomato", 3, 5)
    manager.add_plant("Hops", 6, 6)

    print("\nWatering plants...")
    try:
        manager.watering()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing")
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant healthy...")
    manager.check_health()


if __name__ == "__main__":
    test_garden_management()
