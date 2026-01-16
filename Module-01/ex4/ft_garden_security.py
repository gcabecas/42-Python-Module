class SecurePlant:
    """A plant with protected height and age, validating updates for safety."""

    def __init__(self, name: str) -> None:
        """Initialize a secure plant with a name
        and private height/age values."""
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, height: int) -> None:
        """Set plant height if non-negative, otherwise reject the update."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set plant age if non-negative, otherwise reject the update."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        """Return the current plant height."""
        return self.__height

    def get_age(self) -> int:
        """Return the current plant age."""
        return self.__age


if __name__ == "__main__":
    """Entry point of the program."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(30)
    print("\n")
    plant.set_height(-5)
    plant.__age = -50
    print("\n")
    print(
        f"Current plant: {
            plant.name} ({
            plant.get_height()}cm, {
                plant.get_age()} days)")
