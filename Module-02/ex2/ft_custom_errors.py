class GardenError(Exception):
    """Base garden exception."""
    pass


class PlantError(GardenError):
    """Plant exception."""
    pass


class WaterError(GardenError):
    """Water exception."""
    pass


def test_plant_error() -> None:
    """Demonstrate PlantError."""
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def test_water_error() -> None:
    """Demonstrate WaterError."""
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def test_catching_all_garden_errors() -> None:
    """Demonstrate catching all garden errors."""
    print("Testing catching all garden errors...")

    errors_to_test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]

    for error in errors_to_test:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def main() -> None:
    """Demonstrate custom error types."""
    print("=== Custom Garden Errors Demo ===\n")

    test_plant_error()
    test_water_error()
    test_catching_all_garden_errors()

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
