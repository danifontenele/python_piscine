class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.__name}\n")

    def set_height(self, new_height: int):
        if new_height < 0:
            print("\nInvalid operation attempted: height: "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int):
        if new_age < 0:
            print("Invalid operation attempted: age: "
                  f"{new_age} days old [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    rose = SecurePlant("Rose", 20, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_age(-5)
    rose_name = rose.get_name()
    rose_height = rose.get_height()
    rose_age = rose.get_age()
    print(f"Current plant: {rose_name} ({rose_height}cm, {rose_age} days)")
