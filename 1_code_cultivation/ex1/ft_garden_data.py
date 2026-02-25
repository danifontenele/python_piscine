class Plant:
    def __init__(self, name:    str, height:    int, age:    int):
        self.name = name
        self.height = height
        self.age = age

    def get_description(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(rose.get_description())
    print(sunflower.get_description())
    print(cactus.get_description())
