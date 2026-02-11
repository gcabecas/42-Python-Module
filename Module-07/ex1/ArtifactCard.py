from typing import Any

from ex0.Card import Card, CardType


class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("wrong durability")
        if not isinstance(effect, str) or effect == "":
            raise ValueError("wrong effect")

        self.durability: int = durability
        self.effect: str = effect
        self.card_type = CardType.ARTIFACT

    def activate_ability(self) -> dict[str, Any]:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "destroyed",
            }

        self.durability -= 1

        return {
            "artifact": self.name,
            "activated": True,
            "effect": self.effect,
            "durability_left": self.durability,
            "destroyed": self.durability == 0,
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available = game_state.get("available_mana", 0)
        if not self.is_playable(available):
            raise ValueError("not enough mana to play the card")

        game_state["available_mana"] = available - self.cost

        if "artifacts" not in game_state or not isinstance(
                game_state["artifacts"], list):
            game_state["artifacts"] = []

        game_state["artifacts"].append(self)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }
