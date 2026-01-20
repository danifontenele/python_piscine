class Plant:
	def __init__(self, name:	str, height:	int, age:	int):
		self.name = name
		self.height = height
		self.age = age
	
	def ft_plant_growth(self, days:	int):
		self.init_height = self.height
		self.init_age = self.age

		print("=== Day 1 ===")
		print(f"{self.name}: {self.init_height}cm, {self.init_age} days old")

		self.height += days - 1
		self.age += days - 1
		print(f"=== Day {days} ===")
		print(f"{self.name}: {self.height}cm, {self.age} days old")
		print(f"Growth this week: +{days - 1}cm")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

if __name__ == "__main__":
	rose.ft_plant_growth(5)
