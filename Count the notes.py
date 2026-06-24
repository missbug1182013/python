Amount = int(input("Please Enter The Amount For The Withdrawl :"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10s rupee" , note_3)