def check_temperature(temp_str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    try:
        if temp > 40:
            raise ValueError(
                f"{temp}°C is too hot for plants (max 40°C)\n")
        if temp < 0:
            raise ValueError(
                f"{temp}°C is too cold for plants (min 0°C)\n")
        print(f"Temperature {temp}°C is perfect for plants!\n")
    except ValueError as err:
        print(f"Error: {err}")


def test_temperature_input() -> None:
    tests = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===\n")
    for t in tests:
        check_temperature(t)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
