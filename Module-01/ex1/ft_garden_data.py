class Plant:
    """Represents a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with its name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    """Entry point of the program."""
    print("=== Garden Plant Registry ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    for i in range(3):
        p = plants[i]
        print(f"{p.name}: {p.height}cm, {p.age} days old")
