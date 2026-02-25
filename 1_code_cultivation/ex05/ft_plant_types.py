class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def describe(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def describe(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        shade_area = self.trunk_diameter * 31.3 * self.height
        to_sqr_meter = 10000
        result = int(shade_area / to_sqr_meter)
        print(f"{self.name} provides {result} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def describe(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.age} days, {self.harvest_season}")

    def nutritional_value(self, nutrient: str):
        print(f"{self.name} is rich in vitamin {nutrient}")


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 3000, 21600, 80)
    tomato = Vegetable("tomato", 80, 90, "summer harvest")
    corn = Vegetable("Corn", 2000, 90, "fall")

    print("=== Garden Plant Types ===\n")
    rose.describe()
    rose.bloom()
    print("")
    sunflower.describe()
    sunflower.bloom()
    print("")
    oak.describe()
    oak.produce_shade()
    print("")
    pine.describe()
    pine.produce_shade()
    print("")
    tomato.describe()
    tomato.nutritional_value("vitamin C")
    print("")
    corn.describe()
    corn.nutritional_value("nitrogen")
