import random

from ex0.Card import Card, CardType


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("wrong card")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if not isinstance(card_name, str) or card_name == "":
            raise ValueError("wrong card_name")

        for i, c in enumerate(self.cards):
            if c.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            raise ValueError("deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, float | int]:
        total = len(self.cards)
        if total == 0:
            return {
                "total_cards": 0,
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "average_cost": 0.0,
            }

        creatures = 0
        spells = 0
        artifacts = 0
        cost_sum = 0

        for c in self.cards:
            cost_sum += c.cost
            if c.card_type == CardType.CREATURE:
                creatures += 1
            elif c.card_type == CardType.SPELL:
                spells += 1
            elif c.card_type == CardType.ARTIFACT:
                artifacts += 1

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "average_cost": cost_sum / total,
        }
