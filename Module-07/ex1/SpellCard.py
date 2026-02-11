from typing import Any

from ex0.Card import Card, CardType


class SpellCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect: str) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(effect, str) or effect == "":
            raise ValueError("wrong effect")
        self.effect = effect

        self.card_type = CardType.SPELL
        self.used: bool = False

    def resolve_effect(self, targets: list[str]) -> dict[str, Any]:
        return {
            "effect": self.effect,
            "targets": targets,
            "resolved": True,
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if self.used:
            return {
                "error": "spell already used",
                "card_played": self.name,
                "mana_used": 0,
            }

        available = game_state.get("available_mana", 0)
        if not isinstance(available, int):
            return {
                "error": "wrong game_state",
                "card_played": self.name,
                "mana_used": 0,
            }
        if not self.is_playable(available):
            return {
                "error": "not enough mana to play the card",
                "card_played": self.name,
                "mana_used": 0,
            }

        game_state["available_mana"] = available - self.cost

        targets = game_state.get("targets", [])
        if not isinstance(targets, list):
            targets = []

        self.resolve_effect(targets)

        self.used = True

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }
