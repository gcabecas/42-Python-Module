def list_comp_examples(players, sessions):
    print("=== List Comprehension Examples ===")

    names = sorted([name for name in players.keys()])

    high_scorers = [n for n in names if players[n]["total_score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [players[n]["total_score"] * 2 for n in names]
    print(f"Scores doubled: {scores_doubled}")

    active_players = sorted({s["player"] for s in sessions})
    print(f"Active players: {active_players}")


def dict_comp_examples(players):
    print("\n=== Dict Comprehension Examples ===")

    names = sorted([name for name in players.keys()])

    player_scores = {n: players[n]["total_score"] for n in names}
    print(f"Player scores: {player_scores}")

    totals = [players[n]["total_score"] for n in names]
    score_categories = {
        "high": len([t for t in totals if t >= 8000]),
        "medium": len([t for t in totals if 2000 <= t < 8000]),
        "low": len([t for t in totals if t < 2000]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {n: players[n]["achievements_count"] for n in names}
    print(f"Achievement counts: {achievement_counts}")


def set_comp_examples(sessions, achievements):
    print("\n=== Set Comprehension Examples ===")

    unique_players = {s["player"] for s in sessions}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a for a in achievements}
    print(f"Unique achievements: {unique_achievements}")

    regions = ["north", "east", "central", "north", "east"]
    active_regions = {r for r in regions}
    print(f"Active regions: {active_regions}")


def combined_analysis(players, achievements):
    print("\n=== Combined Analysis ===")

    names = sorted([name for name in players.keys()])
    total_players = len(players)

    total_unique_achievements = len({a for a in achievements})

    totals = [players[n]["total_score"] for n in names]
    avg_score = sum(totals) / len(totals) if len(totals) > 0 else 0.0

    top_score = max(totals) if len(totals) > 0 else 0
    top_names = [n for n in names if players[n]["total_score"] == top_score]
    top_name = sorted(top_names)[0] if len(top_names) > 0 else "none"
    top_ach = (players[top_name]["achievements_count"]
               if top_name in players else 0)

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {avg_score:.1f}")
    print(
        f"Top performer: {top_name} ({top_score} points,"
        f" {top_ach} achievements)")


def main() -> None:
    data = {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5,
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2,
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7,
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4,
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7,
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1,
            },
        },
        'sessions': [
            {
                'player': 'bob',
                'duration_minutes': 94,
                'score': 1831,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'bob',
                'duration_minutes': 32,
                'score': 1478,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 17,
                'score': 1570,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 98,
                'score': 1981,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 15,
                'score': 2361,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'eve',
                'duration_minutes': 29,
                'score': 2985,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 34,
                'score': 1285,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'alice',
                'duration_minutes': 53,
                'score': 1238,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 1555,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'frank',
                'duration_minutes': 92,
                'score': 2754,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 98,
                'score': 1102,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'diana',
                'duration_minutes': 39,
                'score': 2721,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 46,
                'score': 329,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 56,
                'score': 1196,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 117,
                'score': 1388,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'diana',
                'duration_minutes': 118,
                'score': 2733,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 22,
                'score': 1110,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'frank',
                'duration_minutes': 79,
                'score': 1854,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'charlie',
                'duration_minutes': 33,
                'score': 666,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 101,
                'score': 292,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 25,
                'score': 2887,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 53,
                'score': 2540,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'eve',
                'duration_minutes': 115,
                'score': 147,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 118,
                'score': 2299,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 42,
                'score': 1880,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 97,
                'score': 1178,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 18,
                'score': 2661,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 761,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 46,
                'score': 2101,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 117,
                'score': 1359,
                'mode': 'casual',
                'completed': True,
            },
        ],
        'game_modes': [
            'casual',
            'competitive',
            'ranked',
        ],
        'achievements': [
            'first_blood',
            'level_master',
            'speed_runner',
            'treasure_seeker',
            'boss_hunter',
            'pixel_perfect',
            'combo_king',
            'explorer',
        ],
    }

    print("=== Game Analytics Dashboard ===\n")

    list_comp_examples(data["players"], data["sessions"])
    dict_comp_examples(data["players"])
    set_comp_examples(data["sessions"], data["achievements"])
    combined_analysis(data["players"], data["achievements"])


if __name__ == "__main__":
    main()
