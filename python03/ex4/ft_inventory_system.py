import sys


def parse_inventory(args: list) -> dict:
    inventory = {}
    for arg in args:
        parts = arg.split(":")
        obj = parts[0]
        qty = int(parts[1])
        inventory[obj] = qty
    return inventory


def display_inventory(inventory: dict) -> None:
    print("=== Current Inventory ===")
    total_qty = sum(inventory.values())
    inventory = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for obj, qty in inventory:
        percent = (qty / total_qty) * 100
        print(f"{obj}: {qty} units ({percent:.1f}%)")


def inventory_stats(inventory: dict) -> None:
    print("=== Inventory Statistics ===")
    most = max(inventory, key=lambda x: inventory[x])
    least = min(inventory, key=lambda x: inventory[x])
    print(f"Most abundant: {most} ({inventory[most]} units)")
    print(f"Least abundant: {least} ({inventory[least]} units)")


def item_categories(inventory: dict) -> None:
    print("=== Item Categories ===")
    moderate = {}
    scarce = {}
    for obj, qty in inventory.items():
        if qty > 4:
            moderate[obj] = qty
        elif qty <= 4:
            scarce[obj] = qty
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def management_suggestions(inventory: dict) -> None:
    print("=== Management Suggestions ===")
    restock = []
    for obj, qty in inventory.items():
        if qty <= 1:
            restock.append(obj)
    print(f"Restock needed: {', '.join(restock)}")


def dict_properties(inventory: dict) -> None:
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print("Dictionary values:"
          f"{', '.join(str(v) for v in inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory)}\n")
    display_inventory(inventory)
    print()
    inventory_stats(inventory)
    print()
    item_categories(inventory)
    print()
    management_suggestions(inventory)
    print()
    dict_properties(inventory)


if __name__ == "__main__":
    main()
