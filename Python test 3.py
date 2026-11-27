grades = {"Ali": 85,"Rumaysa": 90,"Musfirah": 95,"Afreenish": 80,"Hamna": 75}

total = 0

for score in grades.values():
    total = total + score

average = total / len(grades)
print("Class Average:", average)

top_name = ""
top_score = 0

for name, score in grades.items():
    if score > top_score:
        top_name = name
        top_score = score

print("Highest Scorer:", top_name)
print("Highest Score:", top_score)

student = input("Enter student name: ")
print("Student Score:", grades.get(student, "Not found"))