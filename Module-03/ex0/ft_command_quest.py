import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argc: int = len(sys.argv)
    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {argc}")
