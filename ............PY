 num = int(input("Enter a number: "))

c = 2

while c < num:
    if num % c == 0:
        print("Composite number")
        break
    c = c + 1
else:
    print("Prime number")