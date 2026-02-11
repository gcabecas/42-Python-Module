from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played: int = 0
        self._id_counts: dict[str, int] = {}

    def _make_id(self, card: TournamentCard) -> str:
        base = card.name.split()[-1].lower()
        count = self._id_counts.get(base, 0) + 1
        self._id_counts[base] = count
        return f"{base}_{count:03d}"

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("wrong card")
        card_id = self._make_id(card)
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("unknown card id")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.calculate_rating() >= card2.calculate_rating():
            winner_id, loser_id = card1_id, card2_id
        else:
            winner_id, loser_id = card2_id, card1_id

        winner = self.cards[winner_id]
        loser = self.cards[loser_id]

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list[dict[str, Any]]:
        sorted_cards = sorted(
            self.cards.items(),
            key=lambda pair: pair[1].calculate_rating(),
            reverse=True)
        board: list[dict[str, Any]] = []
        for card_id, card in sorted_cards:
            board.append({
                "id": card_id,
                "name": card.name,
                "rating": card.calculate_rating(),
                "wins": card.wins,
                "losses": card.losses,
            })
        return board

    def generate_tournament_report(self) -> dict[str, Any]:
        total_cards = len(self.cards)
        if total_cards == 0:
            avg_rating = 0
        else:
            avg_rating = sum(
                card.calculate_rating() for card in self.cards.values()
            ) // total_cards
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
