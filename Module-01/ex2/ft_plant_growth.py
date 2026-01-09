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
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)

    start1 = p1.height_cm
    start2 = p2.height_cm

    print("=== Day 1 ===")
    p1.show()
    p2.show()

    i = 0
    while i < 6:
        p1.grow(1)
        p1.age(1)
        p2.grow(2)
        p2.age(1)
        i += 1

    print("=== Day 7 ===")
    p1.show()
    p2.show()

    print("Growth this week: +", p1.height_cm - start1, "cm")
    print("Growth this week: +", p2.height_cm - start2, "cm")
