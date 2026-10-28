("============ SHOPPING RECIPT ============")
valid = False
while not valid:
    try:
        bill =  float(input("Enter the total bill: "))
        discount_percent = float(input("Enter the discount percent: "))
        people = int(input("Enter the number of people: "))
        discount_amount = bill * (discount_percent / 100)
        final_bill = bill - discount_amount
        per_person = final_bill / people 

    except ValueError:
        print("Invalid input! Please type number only!!!!")
    except ZeroDivisionError:
        print("Error: The number of people cannot be 0")

    else:
        print("Final bill after discount", final_bill)
        print("Amount each person pays", per_person)
        valid = True
    finally:
        print("Attempt finished.")
