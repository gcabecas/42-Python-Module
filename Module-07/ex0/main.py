from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        goblin = CreatureCard("Goblin Warrior", 0, "Common", 3, 2)
    except Exception as e:
        print(f"Error creating card: {e}")
        return

    print("\nCard Info:")
    print(dragon.get_card_info())

    game_state = {
        "available_mana": 6,
        "battlefield": []
    }

    print("\nChecking if card is playable with 6 mana:")
    print(dragon.is_playable(game_state["available_mana"]))

    print("\nPlaying card:")
    result = dragon.play(game_state)
    print(result)

    goblin.play(game_state)

    print("\nAttacking target:")
    attack = dragon.attack_target(goblin)
    print(attack)

    print("\nChecking if card is playable with 3 mana:")
    print(dragon.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
