def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def add(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return add


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} enchantment applied to {item}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value):
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    initial_powers = [80, 20, 63]
    power_additions = [13, 12, 12, 10, 6]
    enchantment_types = ['Flowing', 'Dark', 'Earthen']
    items_to_enchant = ['Armor', 'Amulet', 'Shield', 'Sword']

    mage = mage_counter()
    print("Mage Counter:")
    for _ in range(5):
        print(mage())

    print("\nSpell Accumulator:")
    for initial_power in initial_powers:
        print(f"Initial Power: {initial_power}")
        accumulator = spell_accumulator(initial_power)
        for addition in power_additions:
            print(accumulator(addition))
        print()

    print("Enchantment Factory:")
    for enchantment_type in enchantment_types:
        enchant = enchantment_factory(enchantment_type)
        for item in items_to_enchant:
            print(enchant(item))
        print()

    print("Memory Vault:")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    vault["store"]("potion", "Healing Potion")
    print(vault["recall"]("spell"))
    print(vault["recall"]("potion"))
    print(vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
