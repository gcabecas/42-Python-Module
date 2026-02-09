from enum import Enum
from typing import Any

from ex0.Card import Card, CardType


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str) -> None:
        super().__init__(name, cost, rarity)

        try:
            self.effect_type: EffectType = EffectType(effect_type)
        except ValueError:
            raise ValueError("wrong effect_type")

        self.card_type = CardType.SPELL
        self.used: bool = False

    def resolve_effect(self, targets: list[str]) -> dict[str, Any]:
        return {
            "effect_type": self.effect_type.value,
            "targets": targets,
            "resolved": True,
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        if self.used:
            raise ValueError("spell already used")

        available = game_state.get("available_mana", 0)
        if not self.is_playable(available):
            raise ValueError("not enough mana to play the card")

        game_state["available_mana"] = available - self.cost

        targets = game_state.get("targets", [])
        if not isinstance(targets, list):
            targets = []

        effect_result = self.resolve_effect(targets)

        self.used = True

        return {
            "played_card": self.name,
            "mana_used": self.cost,
            "effect": effect_result,
            "consumed": self.used,
        }
