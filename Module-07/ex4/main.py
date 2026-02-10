from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    c1 = TournamentCard("Arena Dragon", 5, "Legendary", 7, 10)
    c2 = TournamentCard("Goblin Champion", 2, "Common", 3, 4)
    c3 = TournamentCard("Knight Elite", 3, "Rare", 4, 6)

    platform.register_card(c1)
    platform.register_card(c2)
    platform.register_card(c3)

    print("Registered cards:")
    for c in platform.cards:
        print(c.get_tournament_stats())

    print("\nSimulating matches...")
    print(platform.simulate_match(c1, c2))
    print(platform.simulate_match(c3, c1))

    print("\nLeaderboard:")
    for row in platform.get_leaderboard():
        print(row)

    print("\nTournament system successfully demonstrated!")


if __name__ == "__main__":
    main()
