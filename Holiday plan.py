print("Holiday Activity Planner")
print("1. Beach")
print("2. Mountain")

choice = int(input("Enter your choice: "))

if (choice == 1):
    print("What type of beach activity?")
    print("1. Adventure")
    print("2. Relaxation")

    choice2 = int(input("Enter your choice2: "))

    if (choice2 == 1):
        print("You have selected Adventure.")
        print("Activity Plan: Go surfing and snorkeling!")
    else:
        print("You have selected Relaxation.")
        print("Activity Plan: Relax on the beach and enjoy the sunset.")

elif (choice == 2):
    print("What type of mountain activity?")
    print("1. Hiking")
    print("2. Camping")

    choice3 = int(input("Enter your choice3: "))

    if (choice3 == 1):
        print("You have selected Hiking.")
        print("Activity Plan: Go hiking and enjoy the beautiful scenery!")
    else:
        print("You have selected Camping.")
        print("Activity Plan: Set up a tent, enjoy a bonfire, and stargaze.")

else:
    print("Wrong choice!")