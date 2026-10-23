import random
while True:
    user_action = input("Enter a choice(rock, paper or scissors)")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou choose {user_action}, computer choose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print ("You win!")
        else:
            print("You loose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
        else:
            print("You loose!")
    elif user_action == "scissors":
            if computer_action == "paper":
                print("You win!")
            else:
                print("You loose!")
    play_again = input("play again? (y/n): ")
    if play_again != "y":
        break