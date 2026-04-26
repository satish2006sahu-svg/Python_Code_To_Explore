import copy


def get_inventory():
    return [
        {"item": "Laptop", "details": {"price": 50000, "stock": 10, "rating": 4.5}},
        {"item": "Phone", "details": {"price": 20000, "stock": 25, "rating": 4.2}},
        {"item": "Tablet", "details": {"price": 15000, "stock": 30, "rating": 4.0}},
        {"item": "Monitor", "details": {"price": 12000, "stock": 15, "rating": 4.8}}
    ]


def apply_discount(data, roll):
    idx = roll % len(data)
    for i in range(len(data)):
        if i == idx:
            data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)
            data[i]["details"]["stock"] -= 5


def compare_data(orig, mod):
    changed = 0
    unchanged = 0
    for i in range(len(orig)):
        if orig[i] == mod[i]:
            unchanged += 1
        else:
            changed += 1
    return changed, unchanged


def main():
    name = "Satish"
    roll = 620

    print("Inventory Tracker")
    print(f"Name: {name}")
    print(f"Roll: {roll}")

    base_inv = get_inventory()
    pure_inv = copy.deepcopy(base_inv)

    shallow_inv = copy.copy(base_inv)
    deep_inv = copy.deepcopy(base_inv)

    target_idx = roll % len(base_inv)
    print(f"\nTargeting index {target_idx} based on roll number {roll}")

    apply_discount(shallow_inv, roll)
    apply_discount(deep_inv, roll)

    print("\nOriginal Inventory:")
    for x in base_inv:
        print(x)

    print("\nShallow Copy:")
    for x in shallow_inv:
        print(x)

    print("\nDeep Copy:")
    for x in deep_inv:
        print(x)

    c, u = compare_data(pure_inv, base_inv)

    if c > 0:
        print("\nCOPY FAILURE DETECTED: Shallow copy has unexpectedly affected the original data!")

    print(f"\nDifferences: {c} items changed unexpectedly in the original data.")
    print(f"Summary Tuple: {(c, u)}")

    print("\nWhy did shallow copy fail?")
    print("Because shallow copy only copies the outer list structure. The inner dictionaries")
    print("are just referenced. When we changed the price in the shallow copy, it edited the")
    print("exact same memory location that the original inventory uses. Deep copy works fine")
    print("because it clones everything, including the inner dictionaries.")


main()
