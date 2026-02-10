from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class CardType(Enum):
    UNKNOWN = "Unknown"
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError("wrong name")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("wrong cost")

        try:
            self.rarity: Rarity = Rarity(rarity)
        except ValueError:
            raise ValueError("wrong rarity")

        self.name: str = name
        self.cost: int = cost
        self.card_type: CardType = CardType.UNKNOWN

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
            "type": self.card_type.value
        }

    def is_playable(self, available_mana: int) -> bool:
        return isinstance(available_mana, int) and available_mana >= self.cost
