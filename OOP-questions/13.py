class Engine:
    def __init__(self, name, power_output):
        self.name= name
        self.power_output = power_output
        
    def start_fan(self):
        return "Engine fan started successfully "
class Car:
    def __init__(self, name):
        self.name = name
        self.engine =Engine(name, "3000 hp")

    def start_car(self):
        return print(self.engine.start_fan())

car1 = Car("Ferarri")
print(f"Car : {car1.name}")
print(f"Car engine : {car1.engine.name}")
car1.start_car()