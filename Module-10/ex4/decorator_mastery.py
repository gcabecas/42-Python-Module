from __future__ import annotations

from functools import wraps
from time import perf_counter, sleep


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = None
            if args:
                if isinstance(args[0], int):
                    power = args[0]
                elif len(args) > 1 and isinstance(args[1], int):
                    power = args[1]

            if power is None:
                power = kwargs.get("power")

            if isinstance(power, int) and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})")
                    attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        cleaned = name.replace(" ", "")
        return cleaned.isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    sleep(0.101)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    if not hasattr(unstable_spell, "_calls"):
        unstable_spell._calls = 0
    unstable_spell._calls += 1
    if unstable_spell._calls < 3:
        raise RuntimeError("boom")
    return "Recovered and cast!"


def main() -> None:
    test_powers = [18, 11, 30, 15]
    spell_names = ['heal', 'fireball', 'lightning', 'tornado']
    mage_names = ['Sage', 'Storm', 'Morgan', 'Jordan', 'Ember', 'Casey']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retry spell...")
    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()

    for name in mage_names:
        print(MageGuild.validate_mage_name(name))
    for name in invalid_names:
        print(MageGuild.validate_mage_name(name))

    print("\nTesting cast_spell with your lists...")
    for i in range(len(test_powers)):
        spell = spell_names[i % len(spell_names)].capitalize()
        power = test_powers[i]
        print(guild.cast_spell(spell, power))

    print("\nTesting insufficient power...")
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
