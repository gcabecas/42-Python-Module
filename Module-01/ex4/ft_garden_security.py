class SecurePlant:
    def __init__(self, name):
        self.name = name
        self._height_cm = 0
        self.__age_days = 0

    def set_height(self, height):
        if height < 0:
            print("Invalid operation attempted: height", height,
                  "cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height_cm = height
            print("Height updated:", height, "cm [OK]")

    def set_age(self, age):
        if age < 0:
            print("Invalid operation attempted: age", age, "days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age_days = age
            print("Age updated:", age, "days [OK]")

    def get_height(self):
        return self._height_cm

    def get_age(self):
        return self.__age_days


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print("Plant created:", plant.name)

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-5)

    print("Current plant:", plant.name, "(", plant.get_height(), "cm,",
          plant.get_age(), "days)")

    plant._age_days = -100

    print("Current plant:", plant.name, "(", plant.get_height(), "cm,",
          plant.get_age(), "days)")

    plant.set_age(3)

    print("Current plant:", plant.name, "(", plant.get_height(), "cm,",
          plant.get_age(), "days)")
