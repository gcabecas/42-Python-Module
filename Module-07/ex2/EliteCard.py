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

        if "battlefield" not in game_state or not isinstance(
                game_state["battlefield"], list):
            game_state["battlefield"] = []

        game_state["battlefield"].append(self)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed",
        }

    def attack(self, target: Any) -> dict[str, Any]:
        damage = self.attack_power
        target_name = getattr(target, "name", str(target))
        if hasattr(target, "health"):
            target.health -= damage
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            return {
                "defender": self.name,
                "damage_taken": 0,
                "damage_blocked": 0,
                "still_alive": True,
            }

        defense = max(1, self.attack_power // 2 + 1)
        blocked = min(incoming_damage, defense)
        damage_taken = incoming_damage - blocked
        self.health = max(0, self.health - damage_taken)

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "attack": self.attack_power,
            "health": self.health,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        if not isinstance(amount, int) or amount <= 0:
            return {
                "channeled": 0,
                "total_mana": self.mana_pool,
            }

        self.mana_pool += amount

        return {
            "channeled": amount,
            "total_mana": self.mana_pool,
        }

    def cast_spell(self, spell_name: str,
                   targets: list[Any]) -> dict[str, Any]:
        if not isinstance(spell_name, str) or spell_name == "":
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [],
                "mana_used": 0,
            }

        if not isinstance(targets, list):
            target_list = [targets]
        else:
            target_list = targets

        mana_cost = max(1, len(target_list) * 2)
        if self.mana_pool < mana_cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [
                    t if isinstance(t, str) else getattr(t, "name", "unknown")
                    for t in target_list],
                "mana_used": 0,
            }

        self.mana_pool -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [
                t if isinstance(t, str) else getattr(t, "name", "unknown")
                for t in target_list],
            "mana_used": mana_cost,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "mana": self.mana_pool,
        }
