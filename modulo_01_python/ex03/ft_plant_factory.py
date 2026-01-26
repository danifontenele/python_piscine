class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory():
    data_list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)]
    instances_list = []
    for name, height, age in data_list:
        instances_list.append(Plant(name, height, age))
    return instances_list


if __name__ == "__main__":
    plants = ft_plant_factory()

    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
