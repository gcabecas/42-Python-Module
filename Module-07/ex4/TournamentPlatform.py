from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: list[TournamentCard] = []

    def register_card(self, card: TournamentCard) -> None:
        if not isinstance(card, TournamentCard):
            raise ValueError("wrong card")
        self.cards.append(card)

    def get_leaderboard(self) -> list[dict[str, Any]]:
        sorted_cards = sorted(
            self.cards,
            key=lambda c: c.calculate_rating(),
            reverse=True)
        board: list[dict[str, Any]] = []
        for c in sorted_cards:
            board.append({
                "name": c.name,
                "rating": c.calculate_rating(),
                "wins": c.wins,
                "losses": c.losses,
            })
        return board

    def simulate_match(self, a: TournamentCard,
                       b: TournamentCard) -> dict[str, Any]:
        if not isinstance(
                a, TournamentCard) or not isinstance(
                b, TournamentCard):
            raise ValueError("wrong match cards")

        rating_a = a.calculate_rating()
        rating_b = b.calculate_rating()

        if rating_a >= rating_b:
            winner, loser = a, b
        else:
            winner, loser = b, a

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
