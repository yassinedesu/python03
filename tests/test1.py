import sys

def display_args(args: list[str]) -> None:
    "Displaying the args with order"
    lenght = len(args)
    i  = 1
    while i < lenght:
        print(args[i])
        i += 1

display_args(sys.argv)
