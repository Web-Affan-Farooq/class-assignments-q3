class Employee:
    def __init__(self,name):
        self.name = name
        self._salary = 10000
        self.__ssn = "bx38473_498"

employee = Employee("affan")
print(f"Employee name : {employee.name} ") # Print name 
print(f"Employee salary : {employee._salary}") # print salary although it's protected
print(f"Employee ssn id : {employee.__ssn}") # Throw attribute error 