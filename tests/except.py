import sys



def hp_tracker(args: list) -> list:
    lst = []
    for i in args[1:]:
        try:
            lst.append(int(i))
        except ValueError:
            print(f"Skipping invalid value: '{i}'")
    return lst

def display_tracker(args: list) -> None:
    lst = hp_tracker(args)
    if len(args) == 1 or not lst:
        print("No valid HP given. Usage: python3 hp_tracker.py <hp1> <hp2> ...")
        sys.exit(1)

    print("=== HP Tracker ===")
    print(f"HP values: {lst}")
    print(f"Players: {len(lst)}")
    print(f"Total HP: {(sum(lst))}")
    print(f"Average HP: {sum(lst) / len(lst)}")
    print(f"Max HP: {max(lst)}")
    print(f"Min HP: {min(lst)}")
    print(f"HP spread: {max(lst) - min(lst)}")

if __name__ == "__main__":
    display_tracker(sys.argv)
