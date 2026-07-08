print("Select yor Ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice:"))

if (choice == 1):
    print("Ehat type of bike? ")
    print("1.Scooty\n")
    print("2.Scooter\n")

    choice2=int(input("Enter your choice2: "))
    if choice==1: 
       print("You have selected scooty")
    else:
        print("You have selected scooter")
elif(choice ==2):
    print("what type of car?")
    print("1. Sedan")
    print("2. XUV")
    choice3=int(input("Enter your choice3: "))
    if choice3==1:
        print("You have selected sedan")
    else:
        print("you have selected XUV")
else:
    print("Wrong choice!")