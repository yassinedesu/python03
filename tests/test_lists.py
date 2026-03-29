import sys

"More like a habit to start with package/library/header"

ls = [42, "Hello", True, 42 / 2]

print("== Before changing the list ==\n")
for i in ls:
    print(i)

print("\n=== After changing the list ===\n")

ls.append("Alice in Bortherland")
ls.append(2026)
ls.append("Adding elements in list")

for i in ls:
    print(f"{i}\n")
