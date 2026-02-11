from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def _format_hand(hand: list) -> str:
    parts: list[str] = []
    for c in hand:
        parts.append(f"{c.name} ({c.cost})")
    return "[" + ", ".join(parts) + "]"


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Supported types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    print(f"Hand: {_format_hand(engine.hand)}")

    result = engine.simulate_turn()

    print("\nTurn execution:")
    print(f"Actions: {result['actions']}")

    status = engine.get_engine_status()
    print(f"\nGame Report: {status}")

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
