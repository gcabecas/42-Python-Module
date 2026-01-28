import sys


def main(argv: list[str]) -> None:
    print("=== Command Quest ===")
    argc: int = len(argv)
    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {argv[i]}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main(sys.argv)
