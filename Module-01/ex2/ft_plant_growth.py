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
    p = Plant("Rose", 25, 30)

    start = p.height_cm

    print("=== Day 1 ===")
    p.show_info()

    for i in range(6):
        p.grow(1)
        p.age(1)

    print("=== Day 7 ===")
    p.show_info()

    print("Growth this week: +", p.height_cm - start, "cm")
