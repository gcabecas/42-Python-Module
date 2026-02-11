from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_templates: list[tuple[Any, ...]] = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 5, 3),
        ]
        self.spell_templates: list[tuple[Any, ...]] = [
            ("Lightning Bolt", 3, "Rare", "Deal 3 damage to target"),
        ]
        self.artifact_templates: list[tuple[Any, ...]] = [
            ("Mana Ring", 2, "Rare", 3, "Permanent: +1 mana per turn"),
        ]

    def get_supported_types(self) -> dict[str, Any]:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(self, name_or_power: Any = None) -> Card:
        if isinstance(
                name_or_power,
                str) and name_or_power.lower() == "goblin":
            n, cost, rarity, atk, hp = self.creature_templates[1]
            return CreatureCard(n, cost, rarity, atk, hp)
        n, cost, rarity, atk, hp = self.creature_templates[0]
        return CreatureCard(n, cost, rarity, atk, hp)

    def create_spell(self, name_or_power: Any = None) -> Card:
        n, cost, rarity, effect = self.spell_templates[0]
        return SpellCard(n, cost, rarity, effect)

    def create_artifact(self, name_or_power: Any = None) -> Card:
        n, cost, rarity, durability, effect = self.artifact_templates[0]
        return ArtifactCard(n, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("wrong size")

        hand: list[Card] = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell(),
        ]

        return {"hand": hand[:size], "battlefield": []}
