from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        goblin = CreatureCard("Goblin Warrior", 0, "Common", 3, 2)
    except Exception as e:
        print(f"Error creating card: {e}")
        return

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    game_state = {
        "available_mana": 6,
        "battlefield": []
    }

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", dragon.is_playable(game_state["available_mana"]))

    result = dragon.play(game_state)
    print("Play result:", result)

    goblin.play(game_state)

    print("\nFire Dragon attacks Goblin Warrior:")
    attack = dragon.attack_target(goblin)
    print("Attack result:", attack)

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", dragon.is_playable(3))

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
