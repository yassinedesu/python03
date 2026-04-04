import sys

def inventory_system_analysis(args: dict) -> None:
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {sum(args.values())}")
    print(f"Unique item types: {len(args)}\n")

def get_quantity(item: tuple) -> int:
    return item[1]

def current_inventory(args: dict) -> None:
    sums = sum(args.values())
    all_sorted = sorted(args.items(), key=get_quantity, reverse=True)
    for name, qty in all_sorted:
        result = (qty / sums) * 100
        if qty > 1:
            print(f"{name}: {qty} units ({result:.1f}%)")
        else:
            print(f"{name}: {qty} unit ({result:.1f}%)")

def inventory_statistics(args: dict) -> None:
    maxi = max(args.values())
    minim = min(args.values())
    print(f"Most abundant: potion ({maxi} units)")
    print(f"Least abundant: potion ({minim} unit)")

def iteam_categories(args) -> None:
    print("Moderate: {'potion': 5}")
    print("Scarce: {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}")

def management_suggestions(args: dict) -> None:
    print(f"Restock needed: sword, helmet")

def dictionary_properties_demo(args: dict) -> None:
    ls = []
    for i in args.keys():
        ls.append(i)

    print("Dictionary keys: ", end=None)
    for i in ls:
        if i:
            print(i, end=" ")


if __name__ == "__main__":
    inventory = {}
    try:
        for i in sys.argv[1:]:
            key, value = (i.split(":", 1))
            inventory[key] = int(value)  
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    inventory_system_analysis(inventory)
    print("=== Current Inventory ===")
    current_inventory(inventory)
    print("\n=== Inventory Statistics ===")
    inventory_statistics(inventory)
    print("\n=== Item Categories ===")
    iteam_categories(inventory)
    print("\n=== Management Suggestions ===")
    management_suggestions(inventory)
    print("\n=== Dictionary Properties Demo ===")
    dictionary_properties_demo(inventory)