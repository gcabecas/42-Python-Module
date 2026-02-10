from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    game_state = {
        "available_mana": 10,
        "battlefield": [],
    }

    elite = EliteCard("Arcane Warrior", 4, "Epic", 6, 12, 2)

    print("\nPlaying EliteCard:")
    play_result = elite.play(game_state)
    print(play_result)

    enemy1 = CreatureCard("Goblin Warrior", 1, "Common", 2, 10)
    enemy2 = CreatureCard("Orc Brute", 2, "Rare", 4, 6)

    print("\nCombat phase:")
    print("Combat stats:", elite.get_combat_stats())
    attack_result = elite.attack(enemy1)
    print(attack_result)
    defend_result = elite.defend(3)
    print(defend_result)

    print("\nMagic phase:")
    print("Magic stats:", elite.get_magic_stats())
    cast_result = elite.cast_spell("Fireball", [enemy1, enemy2])
    print(cast_result)
    channel_result = elite.channel_mana(3)
    print(channel_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
