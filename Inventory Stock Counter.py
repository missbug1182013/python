print("=== Inventory Stock Counter ===")
print("Counting inventory one product at a time.\n")

products = []
total_items = 0
total_boxes = 0

counting = True

while counting:

    name = input("Enter product name: ")
    quantity = int(input(f"Enter total quantity of {name}: "))
    box_size = int(input(f"Enter box size for {name}: "))

    if quantity <= 0 or box_size <= 0:
        print("Invalid input. Quantity and box size must be greater than 0.\n")
        continue

    print(f"\nPacking {name}")
    print("-" * 30)

    remaining = quantity
    boxes = 0

    while remaining >= box_size:
        remaining -= box_size
        boxes += 1

    print("Full boxes :", boxes)
    print("Items left :", remaining)

    products.append({
        "name": name,
        "boxes": boxes,
        "left": remaining
    })

    total_items += quantity
    total_boxes += boxes

    again = input("\nAdd another product? (yes/no): ").strip().lower()

    if again != "yes":
        counting = False

print("\n=== Inventory Stock Report ===")

for product in products:
    print("\nProduct:", product["name"])

    for i in range(1):
        print("Full Boxes :", product["boxes"])
        print("Remaining Items :", product["left"])

print("\n===============================")
print("Total Products :", len(products))
print("Total Full Boxes :", total_boxes)
print("Total Items Counted :", total_items)
print("Inventory counting completed!")