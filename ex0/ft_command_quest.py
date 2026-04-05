import sys


def ft_command_quest(args: list) -> None:
    if len(args) == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print("Total arguments: 1")
        sys.exit(1)
    print(f"Program name: {args[0]}")
    print(f"Arguments received: {len(args) - 1}")
    for i in range(1, len(args)):
        print(f"Argument {i}: {args[i]}")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest(sys.argv)
