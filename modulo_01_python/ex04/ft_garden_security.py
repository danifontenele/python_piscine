class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}\n")

    def set_height(self, new_height: int):
        if new_height < 0:
            print("\nInvalid operation attempted: height: "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, new_age: int):
        if new_age < 0:
            print("Invalid operation attempted: age: "
                  f"{new_age} days old [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.age = new_age
            print(f"Age updated: {self.age} days [OK]")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age


if __name__ == "__main__":
    rose = SecurePlant("Rose", 20, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_age(-5)
    height = rose.get_height()
    age = rose.get_age()
    print(f"Current plant: {rose.name} ({height}cm, {age} days)")
