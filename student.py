student = {}

for i in range(3):
    name = input(f"Enter student name {i+1}: ")
    marks = int(input(f"Enter student marks {i+1}: "))
    student[name] = marks

# Find the topper (student with highest marks)
topper = max(student, key=student.get)

print(f"Top student is {topper} with marks {student[topper]}")
