import sys
import math


def calc() -> None:
    print("=== Game Coordinate System ===\n")
    argc: int = len(sys.argv)
    if argc != 2:
        print("wrong number of args")
        return

    cords: tuple[str] = sys.argv[1].split(",")
    if len(cords) != 3:
        print("Error: Wrong number of cords")
        return

    (x, y, z) = cords
    try:
        dist = math.sqrt((0 - float(x))**2 + (0 - float(y))**2
                         + (0 - float(z))**2)
    except ValueError as err:
        print(f"Error: {err}")
        return

    print(
        f"Distance between (0, 0, 0) and ("
        f"{x}, "
        f"{y}, "
        f"{z}): {dist:.2f}"
    )


if __name__ == "__main__":
    calc()
