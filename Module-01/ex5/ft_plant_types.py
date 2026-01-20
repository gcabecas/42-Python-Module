class Plant:
    """Base plant type storing common data shared by all plants."""

    def __init__(self, name: str, height: int, days: int) -> None:
        """Initialize a plant with a name, height (cm), and age in days."""
        self.name = name
        self.height = height
        self.days = days


class Flower(Plant):
    """A plant that has a flower color and can bloom."""

    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        """Initialize a flower with base plant data plus a flower color."""
        super().__init__(name, height, days)
        self.color = color

    def bloom(self) -> None:
        """Print a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """A plant with a trunk diameter that can produce shade."""

    def __init__(
            self,
            name: str,
            height: int,
            days: int,
            trunk_diameter: int) -> None:
        """Initialize a tree with base plant data plus trunk diameter (cm)."""
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Print an estimated shade area based on trunk diameter."""
        shade = self.trunk_diameter * 156 // 100
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """A plant that can be harvested and has a nutritional value."""

    def __init__(
        self,
        name: str,
        height: int,
        days: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """Initialize a vegetable with harvest season and nutritional value."""
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    """Entry point of the program, do the example."""
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "spring", "vitamin B")

    print()
    print(
        f"{
            rose.name} (Flower): {
            rose.height}cm, {
                rose.days} days, {
                    rose.color} color")
    rose.bloom()
    print(
        f"{tulip.name} (Flower): {tulip.height}cm, {tulip.days} days, "
        f"{tulip.color} color"
    )
    tulip.bloom()

    print()
    print(
        f"{oak.name} (Tree): {oak.height}cm, {oak.days} days, "
        f"{oak.trunk_diameter}cm diameter"
    )
    oak.produce_shade()
    print(
        f"{pine.name} (Tree): {pine.height}cm, {pine.days} days, "
        f"{pine.trunk_diameter}cm diameter"
    )
    pine.produce_shade()

    print()
    print(
        f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.days} days, "
        f"{tomato.harvest_season} harvest"
    )
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print(
        f"{carrot.name} (Vegetable): {carrot.height}cm, {carrot.days} days, "
        f"{carrot.harvest_season} harvest"
    )
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")
