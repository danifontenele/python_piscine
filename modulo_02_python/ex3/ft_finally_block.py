class PlantError(Exception):
    pass


def water_plants(plant_list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise PlantError("Invalid plant!")
            print(f"Watering {plant}")
    except PlantError as e:
        print(f"Error: Cannot water {plant} - {e}!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    plant_list = ["lettuce", "tomato", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    sec_plant_list = ["lettuce", "tomato", None]
    print("Testing with error...")
    water_plants(sec_plant_list)


if __name__ == "__main__":
    test_watering_system()
