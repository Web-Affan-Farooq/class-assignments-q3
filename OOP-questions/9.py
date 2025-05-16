from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        if(int(length) == int(width)):
            print("Length and width of a rectangle are not be equal ...")
        else :
            self.length = length
            self.width = width
            
    def area(self):
        return f"Area of rectangle with width : {self.width} and length : {self.length} is {self.length * self.width}"

r1 = Rectangle(20,6)
print(r1.area()) 