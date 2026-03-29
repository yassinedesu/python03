import sys


def valid_args(args: list) -> list:
    lst = []
    for i in args[1:]:
        try:
            lst.append(int(i))
        except ValueError:
            print(f"Skipping Invalid Value: '{i}'")
    return lst


def ft_score_analytics(args: list) -> None:
    lst = valid_args(args)
    if len(args) == 1 or not lst:
        print("No scores provided. Usage: python3 ft_score_analytics.py ...")
        sys.exit(1)
    print(f"Scores processed: {lst}")
    print(f"Total players: {len(lst)}")
    print(f"Total score: {sum(lst)}")
    print(f"Average score: {sum(lst) / len(lst)}")
    print(f"High score: {max(lst)}")
    print(f"Low score: {min(lst)}")
    print(f"Score range: {max(lst) - min(lst)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics(sys.argv)
