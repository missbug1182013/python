
def calculate_bill(paint, brushes, paper, tax):
    subtotal = paint + brushes + paper
    total = subtotal + (subtotal * tax / 100)
    return total


def factorial(x):
    """This recursive function calculates the factorial of an integer."""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("=== Art Supplies Buying Helper ===")

paint = float(input("Enter paint cost: "))
brushes = float(input("Enter paintbrush cost: "))
paper = float(input("Enter paper cost: "))
tax = float(input("Enter tax percentage: "))

total_bill = calculate_bill(paint, brushes, paper, tax)

print("Total Art Supplies Bill:", total_bill)

print("\n=== Art Supplies Arrangement Helper ===")

supplies = int(input("Enter number of art supplies: "))

print("Factorial function documentation:")
print(factorial.__doc__)

arrangements = factorial(supplies)

print("Number of possible arrangements:", arrangements)
