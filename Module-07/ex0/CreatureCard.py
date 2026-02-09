from typing import Any

from ex0.Card import Card, CardType


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("wrong attack")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("wrong health")

        self.attack: int = attack
        self.health: int = health
        self.card_type = CardType.CREATURE

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available = game_state.get("available_mana", self.cost)
        if not self.is_playable(available):
            raise ValueError("not enough mana to play the card")

        game_state["available_mana"] = game_state["available_mana"] - self.cost
        game_state["battlefield"].append(self.name)

        return {
            'attacker': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to battlefield"
        }

    def attack_target(self, target: Card) -> dict[str, Any]:
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict[str, Any]:
        info = super().get_card_info()
        info["attack"] = self.attack
        info["health"] = self.health
        return info
