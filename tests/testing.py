import sys

total = len(sys.argv)

user_args = len(sys.argv) - 1
if len(sys.argv) == 1:
    print(f"File's name: {sys.argv[0]}, need more args!!")
else:
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"Argument{i}: {arg}")

