class Plant:
    """Represents a plant that can grow and age over time."""

    def __init__(self, name: str, height: int, days: int) -> None:
        """Initialize a plant with a name, height (cm), and age in days."""
        self.name = name
        self.height = height
        self.days = days

    def grow(self, cm: int) -> None:
        """Increase the plant height by `cm`."""
        self.height = self.height + cm

    def age(self, add_days: int) -> None:
        """Increase the plant age by `add_days`."""
        self.days = self.days + add_days

    def get_info(self) -> None:
        """Print the plant information in the required format."""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    """Entry point of the program."""
    rose = Plant("Rose", 25, 30)
    start_height = rose.height

    print("=== Day 1 ===")
    rose.get_info()

    for _ in range(6):
        rose.grow(1)
        rose.age(1)

    print("=== Day 7 ===")
    rose.get_info()

    growth = rose.height - start_height
    print(f"Growth this week: +{growth}cm")
