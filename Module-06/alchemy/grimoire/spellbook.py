def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)

    if result.endswith("INVALID"):
        return "Spell rejected: " + spell_name + " (" + result + ")"
    return "Spell recorded: " + spell_name + " (" + result + ")"
