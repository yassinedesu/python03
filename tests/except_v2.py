import sys

class not_int(ValueError):
    pass


def hp_tracker(args: list) -> None:
    lst = []
    for i in args[1:]:
        try:
            tmp = int(i)
            if not tmp:
                raise not_int(f"Skipping invalid value: '{i}'")
            lst.append(tmp)
        except not_int as e:
            print(f"{e}")
    return lst

def display_tracker(args: list) -> None:
    if len(args) == 1:
        print("No args were given!")
        sys.exit(1)
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
