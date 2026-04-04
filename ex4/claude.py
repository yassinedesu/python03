import sys


def get_quantity(item: tuple) -> int:
    return item[1]


def inventory_system_analysis(args: dict) -> None:
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {sum(args.values())}")
    print(f"Unique item types: {len(args)}\n")


def current_inventory(args: dict) -> None:
    print("=== Current Inventory ===")
    sums = sum(args.values())
    all_sorted = sorted(args.items(), key=get_quantity, reverse=True)
    for name, qty in all_sorted:
        result = (qty / sums) * 100
        unit = "units" if qty > 1 else "unit"
        print(f"{name}: {qty} {unit} ({result:.1f}%)")


def inventory_statistics(args: dict) -> None:
    print("=== Inventory Statistics ===")
    max_item = max(args.items(), key=get_quantity)
    min_item = min(args.items(), key=get_quantity)
    max_unit = "units" if max_item[1] > 1 else "unit"
    min_unit = "units" if min_item[1] > 1 else "unit"
    print(f"Most abundant: {max_item[0]} ({max_item[1]} {max_unit})")
    print(f"Least abundant: {min_item[0]} ({min_item[1]} {min_unit})")


def item_categories(args: dict) -> None:
    print("=== Item Categories ===")
    moderate = {}
    scarce = {}
    for k, v in args.items():
        if v >= 4:
            moderate[k] = v
        else:
            scarce[k] = v
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")


def management_suggestions(args: dict) -> None:
    print("=== Management Suggestions ===")
    restock = []
    for k, v in args.items():
        if v <= 1:
            restock.append(k)
    if restock:
        print(f"Restock needed: {', '.join(restock)}")
    else:
        print("All items well stocked!")


def dictionary_properties_demo(args: dict) -> None:
    print("=== Dictionary Properties Demo ===")
    keys = list(args.keys())
    values = list(args.values())
    value_strs = []
    for v in values:
        value_strs.append(str(v))
    print(f"Dictionary keys: {', '.join(keys)}")
    print(f"Dictionary values: {', '.join(value_strs)}")
    if keys:
        sample = keys[0]
        print(f"Sample lookup - '{sample}' in inventory: {sample in args}")


if __name__ == "__main__":
    inventory = {}
    try:
        for i in sys.argv[1:]:
            key, value = i.split(":", 1)
            inventory[key] = int(value)
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    inventory_system_analysis(inventory)
    current_inventory(inventory)
    print()
    inventory_statistics(inventory)
    print()
    item_categories(inventory)
    print()
    management_suggestions(inventory)
    print()
    dictionary_properties_demo(inventory)