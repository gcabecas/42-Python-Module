def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(artifacts, key=lambda a: a.get("power", 0), reverse=True)
    except (TypeError, AttributeError):
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return [m for m in mages if m.get("power", 0) >= min_power]
    except (TypeError, AttributeError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda s: f"* {s} *", spells))
    except TypeError:
        return []


def mage_stats(mages: list[dict]) -> dict:
    if not isinstance(mages, list) or len(mages) == 0:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    try:
        max_p = max(mages, key=lambda m: m.get("power", 0)).get("power", 0)
        min_p = min(mages, key=lambda m: m.get("power", 0)).get("power", 0)
        total = sum(map(lambda m: m.get("power", 0), mages))
        avg = round(total / len(mages), 2)
        return {"max_power": max_p, "min_power": min_p, "avg_power": avg}
    except (TypeError, AttributeError, ZeroDivisionError):
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}


def main() -> None:
    artifacts = [
        {
            'name': 'Water Chalice', 'power': 71, 'type': 'focus'}, {
            'name': 'Earth Shield', 'power': 120, 'type': 'weapon'}, {
                'name': 'Shadow Blade', 'power': 64, 'type': 'relic'}, {
                    'name': 'Crystal Orb', 'power': 84, 'type': 'focus'}]
    mages = [
        {
            'name': 'Alex', 'power': 83, 'element': 'light'}, {
            'name': 'Casey', 'power': 66, 'element': 'light'}, {
                'name': 'Casey', 'power': 87, 'element': 'earth'}, {
                    'name': 'Luna', 'power': 69, 'element': 'ice'}, {
                        'name': 'Luna', 'power': 85, 'element': 'shadow'}]
    spells = ['shield', 'lightning', 'meteor', 'blizzard']

    sorted_artifacts = artifact_sorter(artifacts)
    powerful_mages = power_filter(mages, 80)
    transformed_spells = spell_transformer(spells)
    stats = mage_stats(mages)

    print("Sorted Artifacts:")
    for a in sorted_artifacts:
        print(f"{a['name']} (Power: {a['power']})")
    print("\nPowerful Mages:")
    for m in powerful_mages:
        print(f"{m['name']} (Power: {m['power']})")
    print("\nTransformed Spells:")
    for s in transformed_spells:
        print(s)
    print("\nMage Stats:")
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Avg Power: {stats['avg_power']}")


if __name__ == '__main__':
    main()
