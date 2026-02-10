# ex2/EliteCard.py
from typing import Any

from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana_pool: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("wrong attack")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("wrong health")
        if not isinstance(mana_pool, int) or mana_pool < 0:
            raise ValueError("wrong mana_pool")

        self.attack_power: int = attack_power
        self.health: int = health
        self.mana_pool: int = mana_pool
        self.card_type = CardType.ELITE

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available = game_state.get("available_mana")
        if not isinstance(available, int):
            raise ValueError("wrong game_state")

        if not self.is_playable(available):
            raise ValueError("not enough mana to play the card")

        game_state["available_mana"] = available - self.cost

        if "battlefield" not in game_state or not isinstance(
                game_state["battlefield"], list):
            game_state["battlefield"] = []

        game_state["battlefield"].append(self)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed",
        }

    def attack(self, target: Card) -> dict[str, Any]:
        damage = self.attack_power

        target.health -= damage
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage,
            "target_health": target.health,
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("wrong incoming_damage")

        self.health = max(0, self.health - incoming_damage)

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "health_left": self.health,
            "defeated": self.health == 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("wrong amount")

        self.mana_pool += amount

        return {
            "card": self.name,
            "channeled": amount,
            "mana_pool": self.mana_pool,
        }

    def cast_spell(self, spell_name: str, targets: Card |
                   list[Card]) -> dict[str, Any]:
        if not isinstance(spell_name, str) or spell_name == "":
            raise ValueError("wrong spell_name")

        if isinstance(targets, list):
            target_list = targets
        else:
            target_list = [targets]

        if self.mana_pool < 1:
            return {
                "caster": self.name,
                "spell": spell_name,
                "success": False,
                "reason": "no mana",
            }

        self.mana_pool -= 1

        names: list[str] = []
        for t in target_list:
            names.append(getattr(t, "name", "unknown"))

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": names,
            "mana_left": self.mana_pool,
            "success": True,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "mana_pool": self.mana_pool,
        }
