class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm):
        self.height_cm = self.height_cm + cm

    def age(self, days):
        self.age_days = self.age_days + days

    def show_info(self):
        print(self.name, ":", self.height_cm, "cm,", self.age_days, "days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")

    count = 0
    for plant in plants:
        print("Created:", plant.name, "(", plant.height_cm, "cm,",
              plant.age_days, "days", ")")
        count += 1

    print("Total plants created:", count)
