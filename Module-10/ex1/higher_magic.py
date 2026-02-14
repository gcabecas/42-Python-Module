def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(target: str) -> str:
        return f"{spell1(target)} and {spell2(target)}"
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(power: int) -> int:
        return base_spell(power) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(power: int) -> str:
        if condition(power):
            return spell(power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(target: str) -> str:
        results = [spell(target) for spell in spells]
        return " -> ".join(results)
    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def damage_spell(power: int) -> int:
    return power


def is_strong(power: int) -> bool:
    return power >= 14


def main() -> None:
    test_values = [11, 14, 15]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    for target in test_targets:
        print(combined(target))

    print("\nTesting power amplifier...")
    for value in test_values:
        amplified = power_amplifier(damage_spell, value)
        print(amplified(10))

    print("\nTesting conditional caster...")
    for value in test_values:
        caster = conditional_caster(is_strong, damage_spell)
        print(caster(value))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for target in test_targets:
        print(sequence(target))


if __name__ == "__main__":
    main()
