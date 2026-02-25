import sys

def ft_score_analytics() -> None:
    scores = []
    prog_name = sys.argv[0]
    ac = len(sys.argv)
    if ac == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        i = 1
        while i < ac:
            try:
                scores.append(int(sys.argv[i]))
            except ValueError:
                print("Caught ValueError: The argument is not a valid number!")
                return
            i += 1
        print(f"Scores processed: {scores}")
        players = ac - 1
        print(f"Total players: {players}")
        total = sum(scores)
        print(f"Total score: {total}")
        average = float(total / players)
        print(f"Average score: {average}")
        higher = max(scores)
        print(f"High score: {higher}")
        lower = min(scores)
        print(f"Low score: {lower}")
        score_range = higher - lower
        print(f"Score range: {score_range}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
