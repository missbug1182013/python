def calculate_bill(food, drinks, dessert, tax):
    subtotal = food + drinks + dessert
    total = subtotal + (subtotal * tax / 100)
    return total


def factorial(x):
    """This recursive function calculates the factorial of an integer."""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("=== Bill & Seating Helper ===")

food = float(input("Enter food cost: "))
drinks = float(input("Enter drinks cost: "))
dessert = float(input("Enter dessert cost: "))
tax = float(input("Enter tax percentage: "))

total_bill = calculate_bill(food, drinks, dessert, tax)

print("Total Bill:", total_bill)

print("\n=== Seating Helper ===")

people = int(input("Enter number of people: "))

print("Factorial function documentation:")
print(factorial.__doc__)

arrangements = factorial(people)

print("Number of seating arrangements:", arrangements)