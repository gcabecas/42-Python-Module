from abc import ABC, abstractmethod
from typing import Any

from ex0.Card import Card


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list[Card],
                     battlefield: list[Card]) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Card]) -> list[Card]:
        pass
