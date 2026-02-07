def validate_ingredients(ingredients: str) -> str:
    parts = ingredients.split(" ")

    valid_ingredients = ["fire", "water", "earth", "air"]
    if all(part in valid_ingredients for part in parts):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
