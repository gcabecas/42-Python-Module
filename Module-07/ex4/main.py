from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    c1 = TournamentCard("Fire Dragon", 5, "Legendary", 7, 10)
    c2 = TournamentCard("Ice Wizard", 3, "Rare", 4, 6)

    id1 = platform.register_card(c1)
    id2 = platform.register_card(c2)

    print("Registering Tournament Cards...\n")
    print(f"\nFire Dragon (ID: {id1}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {c1.calculate_rating()}")
    print(f"- Record: {c1.wins}-{c1.losses}")
    print(f"\nIce Wizard (ID: {id2}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {c2.calculate_rating()}")
    print(f"- Record: {c2.wins}-{c2.losses}")

    print("\nCreating tournament match...")
    match = platform.create_match(id1, id2)
    print(f"Match result: {match}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for idx, row in enumerate(leaderboard, start=1):
        print(
            f"{idx}. {row['name']} - Rating: {row['rating']} "
            f"({row['wins']}-{row['losses']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
