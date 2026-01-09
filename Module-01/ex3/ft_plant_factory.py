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
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Oak", 200, 365),
        Plant("Fern", 10, 60),
    ]

    print("=== Plant Factory Output ===")

    i = 0
    while i < 5:
        plants[i].show_info()
        i = i + 1

    print("Total plants created:", i)
