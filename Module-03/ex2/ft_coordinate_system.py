import sys
import math


def calc() -> None:
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


def noArgs() -> None:
    cords1: tuple[float, float, float] = (10, 20, 5)
    cordsStr = "3,4,0"

    print("Position created: (10, 20, 5)")
    dist = math.sqrt((0 - cords1[0])**2 + (0 - cords1[1])**2
                     + (0 - cords1[2])**2)
    print(f"Distance between (0, 0, 0) and (10, 20, 5): {dist:.2f}\n")

    print("Parsing coordinates: \"3, 4, 0\"")
    cords: tuple[str] = cordsStr.split(",")
    (x, y, z) = cords
    try:
        dist = math.sqrt((0 - float(x))**2 + (0 - float(y))**2
                         + (0 - float(z))**2)
    except ValueError as err:
        print(f"Error: {err}")
    print(f"Distance between (0, 0, 0) and (3, 4, 0): {dist:.2f}\n")
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    cordsStr = "abc,def,ghi"
    cords = cordsStr.split(",")
    (x, y, z) = cords
    try:
        dist = math.sqrt((0 - float(x))**2 + (0 - float(y))**2
                         + (0 - float(z))**2)
    except ValueError as err:
        print(f"Error: {err}\n")

    print("Unpacking demonstration:")
    playerCords: tuple[float, float, float] = (3, 4, 0)
    (x, y, z) = playerCords
    print(f"Player at x={playerCords[0]}, "
          f"y={playerCords[1]}, z={playerCords[2]}")
    print(f"Coordinates: x={x}, y={y}, z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) > 1:
        calc()
    else:
        noArgs()
