# ex3/AggressiveStrategy.py
from typing import Any

from ex0.Card import Card, CardType
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "Aggressive"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        creatures = [t for t in available_targets if not isinstance(t, str)]
        players = [t for t in available_targets if isinstance(t, str)]
        return creatures + players

    def execute_turn(self, hand: list[Card],
                     battlefield: list[Card]) -> dict[str, Any]:
        available_targets = getattr(
            self, "available_targets", ["Enemy Player"])
        targets = self.prioritize_targets(list(available_targets))

        creatures = [c for c in hand if c.card_type == CardType.CREATURE]
        others = [c for c in hand if c.card_type != CardType.CREATURE]
        creatures.sort(key=lambda c: c.cost)

        play_order = creatures + others

        played_cards: list[str] = []
        attacks: list[dict[str, Any]] = []

        for c in play_order:
            played_cards.append(c.name)
            if c.card_type == CardType.CREATURE:
                battlefield.append(c)

        target = targets[0] if len(targets) > 0 else "Enemy Player"
        target_name = target if isinstance(target, str) else target.name

        for c in battlefield:
            if c.card_type == CardType.CREATURE:
                dmg = getattr(c, "attack", 0)
                attacks.append(
                    {"attacker": c.name, "target": target_name, "damage": dmg})

        return {
            "strategy": self.get_strategy_name(),
            "played_cards": played_cards,
            "attacks": attacks,
        }
