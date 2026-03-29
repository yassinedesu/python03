import sys


total = len(sys.argv)
if (total == 1):
    print("No player names provided!")
    print(f"Script: {sys.argv[0]}")
    print("Total: 1")
else:
    print("=== Pixel Greeter ===")
    i = 1
    while i < total:
        print(f"Player {i}: {sys.argv[i]}")
        i += 1
    print(f"Total players: {total - 1}")

