import sys
import math


def calc() -> None:
    print("=== Game Coordinate System ===")
    argc: int = len(sys.argv)
    if argc != 2:
        print("wrong number of args")
    else:
        try:
            cords: tuple = sys.argv[1].split(",")
            if len(cords) != 3:
                raise ValueError(
                    "Wrong number of cords"
                )
        except ValueError as err:
            print(f"Error: {err}")
            return

        (x, y, z) = cords
        try:
            dist = float(math.sqrt(
                (0 - int(x))**2 + (0 - int(y))**2 + (0 - int(z))**2))
        except ValueError as err:
            print(f"Error: {err}")
            return

        print(
            f"Distance between (0, 0, 0) and ("
            f"{x}, "
            f"{y}, "
            f"{z}): {dist:.2f}")


if __name__ == "__main__":
    calc()
