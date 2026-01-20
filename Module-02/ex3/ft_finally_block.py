def water_plants(plant_list: list) -> None:
    """Water plants with cleanup."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    """Test watering system."""
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
