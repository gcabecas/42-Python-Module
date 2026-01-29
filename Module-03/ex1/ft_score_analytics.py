import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv)
    args: list[int] = []

    if argc == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ..."
        )
    else:
        print("Scores processed: [", end="")
        for i in range(1, argc):
            try:
                score = int(sys.argv[i])
            except ValueError:
                print("]")
                print(f"Error: Invalid score '{sys.argv[i]}'")
                return
            args.append(score)

            print(f"{score}", end="")
            if i != argc - 1:
                print(", ", end="")
            print("]")

            total_players: int = argc - 1
            total_score: int = sum(args)
            high_score: int = max(args)
            low_score: int = min(args)

            print(f"Total players: {total_players}")
            print(f"Total score: {total_score}")
            print(f"Average score: {total_score / total_players}")
            print(f"High score: {high_score}")
            print(f"Low score: {low_score}")
            print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
