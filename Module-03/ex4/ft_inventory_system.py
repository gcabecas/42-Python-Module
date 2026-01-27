import sys


def main() -> None:
    inv = dict()
    argc = len(sys.argv)
    tot = 0
    for arg in sys.argv[1:]:
        if ":" not in arg:
            continue
        key, cont = arg.split(":", 1)
        try:
            count = int(cont)
        except ValueError:
            continue
        tot += count
        inv[key] = count
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {tot}")
    print(f"Unique item types: {argc - 1}")
    print("\n=== Current Inventory ===")

    if tot == 0:
        print("\n=== Current Inventory ===")
        print("No items provided.")
        return

    sorted_inv = dict(sorted(inv.items(), key=lambda kv: kv[1], reverse=True))

    for name, count in sorted_inv.items():
        unit_word = "units" if count != 1 else "unit"
        percent = count / tot * 100
        print(f"{name}: {count} {unit_word} ({percent:.1f}%)")

    items_list = list(sorted_inv.items())
    most_name, most_count = items_list[0]
    least_name, least_count = items_list[-1]

    print("\n=== Inventory Statistics ===")
    most_unit = "units" if most_count != 1 else "unit"
    least_unit = "units" if least_count != 1 else "unit"
    print(f"Most abundant: {most_name} ({most_count} {most_unit})")
    print(f"Least abundant: {least_name} ({least_count} {least_unit})")

    print("\n=== Item Categories ===")


if __name__ == "__main__":
    main()
