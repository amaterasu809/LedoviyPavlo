class Student:
    def __init__(self, name, age, groupID):
        self.name = name
        self.age = age
        self.groupID = groupID

    def __str__(self):
        return f'{self.name}, {self.age}, {self.groupID}'
    
student1 = Student("Pasha", 18, "KB-221")

print(student1)