class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height_cm}cm, {p1.age_days} days old")
    print(f"{p2.name}: {p2.height_cm}cm, {p2.age_days} days old")
    print(f"{p3.name}: {p3.height_cm}cm, {p3.age_days} days old")
