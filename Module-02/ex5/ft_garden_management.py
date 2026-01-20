class GardenError(Exception):
    """Base garden exception."""
    pass


class PlantError(GardenError):
    """Plant exception."""
    pass


class WaterError(GardenError):
    """Water exception."""
    pass


class Plant:
    """Plant class."""

    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        """Initialize plant."""
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Garden manager."""

    def __init__(self) -> None:
        """Initialize garden manager."""
        self.plants: list = []
        self.water_tank_level: int = 10

    def add_plant(self, name: str, water_level: int = 5,
                  sunlight_hours: int = 8) -> None:
        """Add plant to garden."""
        if not name or name.strip() == "":
            raise PlantError("Plant name cannot be empty!")

        plant = Plant(name, water_level, sunlight_hours)
        self.plants.append(plant)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Water all plants."""
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> None:
        """Check plant health."""
        plant = None
        for p in self.plants:
            if p.name == plant_name:
                plant = p
                break

        if plant is None:
            raise PlantError(f"Plant '{plant_name}' not found in garden")

        water = plant.water_level
        sunlight = plant.sunlight_hours

        if water < 1 or water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")

        if sunlight < 2 or sunlight > 12:
            raise ValueError(f"Sunlight hours {sunlight} is invalid")

        print(f"{plant_name}: healthy (water: {water}, sun: {sunlight})")

    def set_water_tank_level(self, level: int) -> None:
        """Set the water tank level."""
        self.water_tank_level = level

    def check_water_tank(self) -> None:
        """Check water tank level."""
        if self.water_tank_level < 5:
            raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    """Test garden management system."""
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("\nAdding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        garden.add_plant("lettuce", 15, 6)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        garden.add_plant("", 5, 8)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    garden.water_plants()

    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato")
    except (PlantError, ValueError) as e:
        print(f"Error checking tomato: {e}")

    try:
        garden.check_plant_health("lettuce")
    except (PlantError, ValueError) as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        garden.set_water_tank_level(3)
        garden.check_water_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
