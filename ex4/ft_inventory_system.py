import sys

def inventory_system_analysis(args: dict) -> None:
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {sum(args.values())}")
    print(f"Unique item types: {len(args)}\n")

def current_inventory(args: dict) -> None:
    print("=== Current Inventory ===")
    all_sorted = sorted(args.items(), reverse=True)
    for i in all_sorted:
        print(i)

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
    current_inventory(inventory)