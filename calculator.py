def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a*b


def division(a, b):
  if b == 0:
    return "Error! Division by zero is not allowed."
  return a / b


# Display menu options
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter a number (1-4): "))

if choice in [1, 2, 3, 4]:
  # Collect two numbers properly and convert them to floats
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  if choice == 1:
    result = add(num1, num2)
    print("The result is:", result)
  elif choice == 2:
    result = subtract(num1, num2)
    print("The result is:", result)
  elif choice == 3:
    result = multiply(num1, num2)
    print("The result is:", result)
  elif choice == 4:
    result = division(num1, num2)
    print("The result is:", result)
else:
  print("Invalid choice! Please type a number between 1 and 4.")