class Plant:
    """Base plant with height tracking and growth accumulation."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with a name and starting height (cm)."""
        self.name = name
        self.height = height
        self.growth = 0

    def grow(self, cm: int) -> None:
        """Increase height by `cm` and store the growth amount."""
        self.height += cm
        self.growth += cm


class FloweringPlant(Plant):
    """A plant subtype that has a flower color."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant with a color."""
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """A flowering plant subtype that has prize points."""

    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        """Initialize a prize flower with prize points."""
        super().__init__(name, height, color)
        self.prize_points = prize_points


class Garden:
    """A garden owned by someone, storing a collection of plants."""

    def __init__(self, owner: str) -> None:
        """Initialize a garden for a given owner."""
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden and print a confirmation."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self) -> None:
        """Grow every plant in the garden by 1cm and print progress."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            print(f"{plant.name} grew 1cm")


class GardenManager:
    """Manages multiple gardens and provides analytics via nested stats."""

    class GardenStats:
        """Statistics helper for computing analytics on a garden."""

        def plants_added(self, garden: "Garden") -> int:
            """Return the number of plants in the given garden."""
            count = 0
            for _ in garden.plants:
                count += 1
            return count

        def total_growth(self, garden: "Garden") -> int:
            """Return the total accumulated growth for all
            plants in a garden."""
            total = 0
            for plant in garden.plants:
                total += plant.growth
            return total

        def plant_types(self, garden: "Garden") -> tuple:
            """Return a tuple of (regular, flowering, prize) plant counts."""
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if plant.__class__ is PrizeFlower:
                    prize += 1
                elif plant.__class__ is FloweringPlant:
                    flowering += 1
                else:
                    regular += 1
            return (regular, flowering, prize)

    def __init__(self) -> None:
        """Initialize the manager with an empty garden list
        and stats helper."""
        self.gardens = []
        self.stats = GardenManager.GardenStats()

    def add_garden(self, garden: Garden) -> None:
        """Register a garden in the manager."""
        self.gardens.append(garden)

    def get_garden(self, owner: str) -> Garden:
        """Return the garden for the given owner (fallback to first garden)."""
        for garden in self.gardens:
            if garden.owner == owner:
                return garden
        return self.gardens[0]

    def total_gardens(self) -> int:
        """Return the number of gardens managed."""
        count = 0
        for _ in self.gardens:
            count += 1
        return count

    @classmethod
    def create_garden_network(cls):
        """Create a demo network of gardens and return a ready manager."""
        manager = cls()
        alice = Garden("Alice")
        bob = Garden("Bob")
        bob.plants.append(Plant("Bonsai", 92))
        manager.add_garden(alice)
        manager.add_garden(bob)
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate that a plant height is not negative."""
        return height >= 0

    @staticmethod
    def garden_score(garden: Garden) -> int:
        """Compute a score from heights and prize points for a garden."""
        score = 0
        for plant in garden.plants:
            score += plant.height
            if plant.__class__ is PrizeFlower:
                score += plant.prize_points * 4
        return score


if __name__ == "__main__":
    """Entry point of the program."""
    print("=== Garden Management System Demo ===")
    print()

    manager = GardenManager.create_garden_network()
    alice = manager.get_garden("Alice")
    bob = manager.get_garden("Bob")

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    print()
    alice.help_all_grow()
    print()

    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in alice.plants:
        if plant.__class__ is PrizeFlower:
            print(
                f"- {plant.name}: {plant.height}cm, "
                f"{plant.color} flowers (blooming), "
                f"Prize points: {plant.prize_points}"
            )
        elif plant.__class__ is FloweringPlant:
            print(
                f"- {plant.name}: {plant.height}cm, "
                f"{plant.color} flowers (blooming)")
        else:
            print(f"- {plant.name}: {plant.height}cm")

    added = manager.stats.plants_added(alice)
    growth = manager.stats.total_growth(alice)
    regular, flowering, prize = manager.stats.plant_types(alice)

    print()
    print(f"Plants added: {added}, Total growth: {growth}cm")
    print(
        f"Plant types: {regular} regular, "
        f"{flowering} flowering, {prize} prize flowers")
    print()

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    alice_score = GardenManager.garden_score(alice)
    bob_score = GardenManager.garden_score(bob)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {manager.total_gardens()}")
