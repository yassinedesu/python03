import sys


def hp_tracker(args: list) -> None:
    i = 1
    lst = []
    while i < len(args):
        if args[i].isdigit():
            lst.append(int(args[i]))
        i += 1
    return lst


def display_tracker(args: list) -> None:
    if len(args) == 1:
        print("No args were given!")
        sys.exit(1)

    for i in args[1:]:
        if not i.isdigit():
            print(f"Skipping invalid value: '{i}'")
            
    lst = hp_tracker(args)

    print("=== HP Tracker ===")
    print(f"HP values: {lst}")
    print(f"Players: {len(lst)}")
    print(f"Total HP: {float((sum(lst)))}")
    print(f"Average HP: {float(sum(lst) / len(lst))}")
    print(f"Max HP: {max(lst)}")
    print(f"Min HP: {min(lst)}")
    print(f"HP spread: {max(lst) - min(lst)}")

if __name__ == "__main__":
    display_tracker(sys.argv)
