class GardenManager:
    gardens_list = []
    total = 0

    @classmethod
    def create_garden_network(cls):
        gardens = [Garden("Daniel"),
                   Garden("Alice"),
                   Garden("Wesley")]
        cls.total = 0
        cls.gardens_list = []
        for garden in gardens:
            cls.gardens_list.append(garden)
            cls.total += 1

    @classmethod
    def compare_gardens(cls, garden1, garden2):
        cls.garden1 = garden1
        cls.garden2 = garden2
        garden1_score = GardenStats.garden_score(cls.garden1.plant_list)
        garden2_score = GardenStats.garden_score(cls.garden2.plant_list)
        print(f"Garden scores - {cls.garden1.name}: {garden1_score}, "
              f"{cls.garden2.name}: {garden2_score}")


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plant_list = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plant_list.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all_plants(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plant_list:
            plant.grow()
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def get_stats(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plant_list:
            GardenStats.plant_description(plant)
        print(f"\nPlants added: {GardenStats.total_plants(self.plant_list)}, "
              f"Total growth: {self.total_growth}")
        regular, flowering, prize = GardenStats.count_types(self.plant_list)
        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, "
              f"{prize} prize flowers")


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str,
                 height: int, age: int,
                 color: str, points: int):
        super().__init__(name, height, age, color)
        self.points = points


class GardenStats:
    @staticmethod
    def plant_description(plant):
        if isinstance(plant, PrizeFlower):
            if plant.is_blooming is True:
                print(f"{plant.name}: "
                      f"{plant.height}cm, "
                      f"{plant.color} flowers (blooming), "
                      f"{plant.points} prize points")
            else:
                print(f"{plant.name}: "
                      f"{plant.height}cm, "
                      f"{plant.color} flowers, "
                      f"{plant.points} prize points")
        elif isinstance(plant, FloweringPlant):
            if plant.is_blooming is True:
                print(f"{plant.name}: "
                      f"{plant.height}cm, "
                      f"{plant.color} flowers (blooming)")
            else:
                print(f"{plant.name}: "
                      f"{plant.height}cm, "
                      f"{plant.color} flowers")
        elif isinstance(plant, Plant):
            print(f"{plant.name}: {plant.height}cm")

    @staticmethod
    def total_plants(plant_list):
        count = 0
        for plants in plant_list:
            count += 1
        return count

    @staticmethod
    def count_types(plant_list):
        nplant = 0
        flowering = 0
        prize = 0
        for plant in plant_list:
            if isinstance(plant, PrizeFlower):
                prize += 1
            elif isinstance(plant, FloweringPlant):
                flowering += 1
            elif isinstance(plant, Plant):
                nplant += 1
        return nplant, flowering, prize

    @staticmethod
    def garden_score(plant_list):
        total_score = 0
        for plant in plant_list:
            if isinstance(plant, PrizeFlower):
                total_score += plant.points
            total_score += plant.height
        return total_score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    GardenManager.create_garden_network()

    garden1 = GardenManager.gardens_list[0]
    garden2 = GardenManager.gardens_list[1]
    garden3 = GardenManager.gardens_list[2]
    print("")
    rose = FloweringPlant("Rose", 25, 30, "red")
    oak = Plant("Oak Tree", 200, 365)
    sunflower = PrizeFlower("Sunflower", 80, 45, "yellow", 10)
    garden2.add_plant(oak)
    garden2.add_plant(rose)
    garden2.add_plant(sunflower)
    print("")
    garden2.grow_all_plants()
    print("")
    rose.bloom()
    sunflower.bloom()
    garden2.get_stats()
    print("")
    print(f"Total gardens managed: {GardenManager.total}")
    GardenManager.compare_gardens(garden1, garden2)
