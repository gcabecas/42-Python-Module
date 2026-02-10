import random
from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.registry: dict[str, list[tuple[Any, ...]]] = {
            "creature": [],
            "spell": [],
            "artifact": [],
        }

        self.register("creature", ("Goblin Warrior", 2, "Common", 2, 3))
        self.register("creature", ("Fire Dragon", 5, "Legendary", 7, 5))

        self.register("spell", ("Fireball", 4, "Rare", "damage"))
        self.register("spell", ("Ice Lance", 3, "Common", "damage"))
        self.register("spell", ("Lightning Bolt", 3, "Rare", "damage"))

        self.register("artifact", ("Mana Ring", 2, "Rare",
                      3, "Permanent: +1 mana per turn"))
        self.register("artifact", ("Wizard Staff", 4, "Epic",
                      2, "Permanent: spells deal +1 damage"))
        self.register(
            "artifact",
            ("Arcane Crystal",
             3,
             "Common",
             3,
             "Permanent: +1 mana_pool"))

    def register(self, kind: str, template: tuple[Any, ...]) -> None:
        self.registry[kind].append(template)

    def get_supported_types(self) -> dict[str, Any]:
        return {
            "creatures": [t[0] for t in self.registry["creature"]],
            "spells": [t[0] for t in self.registry["spell"]],
            "artifacts": [t[0] for t in self.registry["artifact"]],
        }

    def create_creature(self, name_or_power: Any = None) -> Card:
        n, cost, rarity, atk, hp = random.choice(self.registry["creature"])
        return CreatureCard(n, cost, rarity, atk, hp)

    def create_spell(self, name_or_power: Any = None) -> Card:
        n, cost, rarity, effect_type = random.choice(self.registry["spell"])
        return SpellCard(n, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: Any = None) -> Card:
        n, cost, rarity, durability, effect = random.choice(
            self.registry["artifact"])
        return ArtifactCard(n, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("wrong size")

        hand: list[Card] = []
        for _ in range(size):
            kind = random.choice(["creature", "spell", "artifact"])
            if kind == "creature":
                hand.append(self.create_creature())
            elif kind == "spell":
                hand.append(self.create_spell())
            else:
                hand.append(self.create_artifact())

        return {"hand": hand, "battlefield": []}
