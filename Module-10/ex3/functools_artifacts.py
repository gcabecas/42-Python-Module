from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }

    func = ops.get(operation)
    if func is None:
        return 0

    return reduce(func, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast(value):
        return "Unknown spell"

    @cast.register
    def _(value: int):
        return f"Damage spell: {value}"

    @cast.register
    def _(value: str):
        return f"Enchantment: {value}"

    @cast.register
    def _(value: list):
        return [cast(v) for v in value]

    return cast


def base_enchantment(power: int, element: str) -> str:
    return f"Enchantment with {power} power and {element} element."


def main() -> None:
    spell_powers = [37, 34, 46, 41, 16, 21]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [9, 20, 12]

    print("Testing spell reducer...")
    for operation in operations:
        result = spell_reducer(spell_powers, operation)
        print(f"{operation.capitalize()}: {result}")

    print("\nTesting partial enchanter...")

    enchanter = partial_enchanter(base_enchantment)
    for enchantment_name, enchantment_func in enchanter.items():
        print(f"{enchantment_name}: {enchantment_func()}")

    print("\nTesting memoized Fibonacci...")
    for n in fibonacci_tests:
        print(f"Fibonacci({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("Invisibility"))
    print(dispatcher([10, "Strength", 20]))


if __name__ == "__main__":
    main()
