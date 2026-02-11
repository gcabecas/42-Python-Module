from typing import Any

from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("wrong attack")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("wrong health")

        self.attack_power: int = attack_power
        self.health: int = health
        self.card_type = CardType.CREATURE

        self.wins: int = 0
        self.losses: int = 0

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
            "effect": "Tournament card deployed",
        }

    def attack(self, target: Card) -> dict[str, Any]:
        damage = self.attack_power
        if hasattr(
                target,
                "health") and isinstance(
                getattr(
                target,
                "health"),
                int):
            target.health = max(0, target.health - damage)
            return {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": damage,
                "target_health": target.health,
            }
        return {
            "attacker": self.name,
            "target": getattr(target, "name", "unknown"),
            "damage_dealt": damage,
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
        return {"attack_power": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        return 1000 + (self.wins * 50) - (self.losses * 30)

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("wrong wins")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("wrong losses")
        self.losses += losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        info = self.get_card_info()
        info.update(self.get_combat_stats())
        info.update(self.get_rank_info())
        return info
