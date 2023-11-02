class Student: 
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name}, {self.age}'
    
students = [
    Student("Andriy", 20),
    Student("Pasha", 18),
    Student("Denis", 19)    
    ]

students = sorted(students, key=lambda x: x.age)
for student in students:
    print(f"Students name is {student.name}, age is {student.age}")
        