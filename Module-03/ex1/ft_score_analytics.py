import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv)
    args: list = []
    if argc == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ...")
    else:
        print("Scores processed: [", end="")
        for i in range(1, argc):
            args.append(int(sys.argv[i]))
            print(f"{sys.argv[i]}", end="")
            if i != argc - 1:
                print(", ", end="")
        print("]")
        print(f"Total players: {argc - 1}")
        print(f"Total score: {sum(args)}")
        print(f"Average score: {sum(args) / (argc - 1)}")
        print(f"High score: {max(args)}")
        print(f"Low score: {min(args)}")
        print(f"Score range: {max(args) - min(args)}")
