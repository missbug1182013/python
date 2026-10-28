import math
import random

print("===== LUCKY NUMBER CALCULATOR =====")

# 1. Generate a lucky number
lucky_number = random.randint(1, 10)
print("\nYour lucky number is:", lucky_number)

activities = [
    "Read a book",
    "Play a game",
    "Listen to music",
    "Go for a walk",
    "Watch a movie"
]

activity = random.choice(activities)
print("Your random activity is:", activity)


print("\n===== NUMBER GUESSING GAME =====")
import random
playing = True
number = str(random.randint(0,9))
print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Give me your best gues! \n")
    if number == guess:
        print("You win the game!")
        print("The number was", number)
        break
    else:
        print("Try again.\n")
print("\n===== MATH CALCULATOR =====")

x = float(input("Enter a decimal number: "))
y = float(input("Enter another number: "))

print("Ceiling value of", x, ":", math.ceil(x))
print("Floor value of", x, ":", math.floor(x))

print("Absolute value of", x, ":", math.fabs(x))
print("Absolute value of", y, ":", math.fabs(y))

print("Copy sign value:", math.copysign(abs(x), y))
print("GCD of", int(x), "and", int(y), ":", math.gcd(int(x), int(y)))

print("\n===== FUN GAMES =====")
print("Lucky number:", lucky_number)
print("Random activity:", activity)
print("Guessing game completed!")
print("Math calculations completed!")
print("Thank you for playing!")