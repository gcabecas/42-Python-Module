from typing import Any

from ex0.Card import Card, CardType
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

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

        mana_pool = 5
        mana_used = 0
        played_cards: list[str] = []
        damage_dealt = 0

        for c in play_order:
            if mana_used + c.cost > mana_pool:
                continue
            played_cards.append(c.name)
            mana_used += c.cost
            if c.card_type == CardType.CREATURE:
                battlefield.append(c)
                damage_dealt += getattr(c, "attack", 0)
            elif c.card_type == CardType.SPELL:
                damage_dealt += 3

        target = targets[0] if len(targets) > 0 else "Enemy Player"
        target_name = target if isinstance(target, str) else target.name

        return {
            "cards_played": played_cards,
            "mana_used": mana_used,
            "targets_attacked": [target_name],
            "damage_dealt": damage_dealt,
        }
