secret = 27
attempts = 5

while attempts > 0:
    print("Lives:", attempts)

    guess = int(input("Guess the number between 1 and 50: "))

    if guess == secret:
        print("You won! 💐🥳")
        break
    else:
        diff = abs(secret - guess)

        if diff <= 3:
            print("You are hot! 🔥")
        elif diff <= 8:
            print("You are warm! ♨️")
        elif diff <= 16:
            print("You are cold! 🧊")
        else:
            print("You are ice cold! 🥶❄️")

    attempts -= 1
    print()

if attempts == 0:
    print("GAME OVERRRRRRRRR! The secret number was", secret)