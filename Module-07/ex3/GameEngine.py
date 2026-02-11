from typing import Any

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

        self.hand: list = []
        self.battlefield: list = []

        self.turns_simulated: int = 0
        self.cards_created: int = 0
        self.total_damage: int = 0

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        themed = factory.create_themed_deck(3)
        self.hand = themed.get("hand", [])
        self.battlefield = themed.get("battlefield", [])
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise ValueError("engine not configured")

        self.strategy.available_targets = ["Enemy Player"]

        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += actions.get("damage_dealt", 0)

        return {
            "actions": actions,
            "turns_simulated": self.turns_simulated,
        }

    def get_engine_status(self) -> dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (
                self.strategy.get_strategy_name()
                if self.strategy is not None else "None"),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
