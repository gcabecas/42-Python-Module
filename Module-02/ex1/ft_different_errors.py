def test_value_error() -> None:
    """Demonstrate ValueError."""
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")


def test_zero_division_error() -> None:
    """Demonstrate ZeroDivisionError."""
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")


def test_file_not_found_error() -> None:
    """Demonstrate FileNotFoundError."""
    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")


def test_key_error() -> None:
    """Demonstrate KeyError."""
    print("Testing KeyError...")
    try:
        garden_plants = {"tomato": 5, "lettuce": 3}
        garden_plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_multiple_errors() -> None:
    """Demonstrate catching multiple error types."""
    print("Testing multiple errors together...")

    try:
        int("invalid")
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!\n")


def garden_operations() -> None:
    """Main function demonstrating different error types."""
    print("=== Garden Error Types Demo ===")

    test_value_error()
    test_zero_division_error()
    test_file_not_found_error()
    test_key_error()
    test_multiple_errors()

    print("All error types tested successfully!")


def test_error_types() -> None:
    """Test different error types."""
    garden_operations()


if __name__ == "__main__":
    test_error_types()
