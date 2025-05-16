class Student:
    def __init__(self, name:str, marks:int) -> None:
        self.name:str = name
        self.marks :int= marks
    
    def display(self) -> None:
        print({
            "Student name ": self.name,
            "Marks":self.marks
        })
    
s1 = Student("affan",20)
s1.display()