class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject

t1 = Teacher("Affan", "Physics")
print(t1.name)    
print(t1.subject) 