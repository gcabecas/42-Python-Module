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

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        themed = factory.create_themed_deck(3)
        self.hand = themed.get("hand", [])
        self.battlefield = themed.get("battlefield", [])

    def simulate_turn(self) -> dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise ValueError("engine not configured")

        # let strategy know possible targets (simple)
        self.strategy.available_targets = ["Enemy Player"]

        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1

        return {
            "actions": actions,
            "turns_simulated": self.turns_simulated,
        }

    def get_engine_status(self) -> dict[str, Any]:
        return {
            "configured": self.factory is not None and self.strategy
            is not None,
            "turns_simulated": self.turns_simulated,
            "hand_size": len(
                self.hand),
            "battlefield_size": len(
                self.battlefield),
        }
