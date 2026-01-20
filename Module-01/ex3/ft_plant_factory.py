class Plant:
    """Represents a plant created from factory specifications."""

    def __init__(self, name: str, height: int, days: int) -> None:
        """Initialize a plant with its name, height, and age in days."""
        self.name = name
        self.height = height
        self.days = days


if __name__ == "__main__":
    """Entry point of the program, do the example."""
    print("=== Plant Factory Output ===")

    specs = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []
    for i in range(5):
        name, height, days = specs[i]
        p = Plant(name, height, days)
        plants.append(p)
        print(f"Created: {p.name} ({p.height}cm, {p.days} days)")
