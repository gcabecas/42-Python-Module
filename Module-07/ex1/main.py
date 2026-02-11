from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()

    spell = SpellCard("Lightning Bolt", 3, "Rare", "Deal 3 damage to target")
    artifact = ArtifactCard(
        "Mana Crystal",
        2,
        "Common",
        3,
        "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    stats = deck.get_deck_stats()

    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:\n")

    game_state = {
        "available_mana": 10,
        "battlefield": [],
        "artifacts": [],
        "targets": ["target"],
    }

    for _ in range(3):
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.card_type.value})")
        result = card.play(game_state)
        print(f"Play result: {result}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
