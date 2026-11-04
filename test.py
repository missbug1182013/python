def add(a, b):
    return(a+b)
def subtract(a, b):
    return(a-b)
def multiply(a, b):
    return(a*b)
def division(a, b):
    return(a/b)
num = int(input("Enter a number 1-4:"))
if num == 1:
    float(input("Give any two numbers:"))
    num == input
    result = add(num)
    print("The result is:", result)
elif num == 2:
    float(input("Give any two numbers:"))
    num == input
    result = subtract(num)
    print("The result is:", result)
elif num == 3:
    float(input("Give any two numbers:"))
    num == input
    result = multiply(num)
    print("The result is:", result)
elif num == 4:
    float(input("Give any two numbers:"))
    num == input
    result = division(num)
    print("The result is:", result)
else:
    print("Type a number:")
