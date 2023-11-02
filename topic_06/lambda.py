students = []

file = open("topic_06\students.txt")
for line in file:
    name, mark = line.rstrip().split(",")
        
    student = {} 
    student["name"] = name
    student["mark"] = mark        
    students.append(student)

for student in sorted(students, key=lambda x: x["mark"]):
    print(f"Name is {student['name']} mark is {student['mark']}") 