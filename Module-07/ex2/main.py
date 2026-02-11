from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    game_state = {
        "available_mana": 10,
        "battlefield": [],
    }

    elite = EliteCard("Arcane Warrior", 4, "Epic", 5, 10, 8)

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    elite.play(game_state)

    enemy1 = CreatureCard("Enemy", 1, "Common", 2, 10)
    enemy2 = CreatureCard("Enemy", 1, "Common", 2, 10)

    print("Combat phase:")
    attack_result = elite.attack(enemy1)
    print("Attack result:", attack_result)
    defend_result = elite.defend(5)
    print("Defense result:", defend_result)

    print("\nMagic phase:")
    _ = enemy2
    cast_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", cast_result)
    channel_result = elite.channel_mana(3)
    print("Mana channel:", channel_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
