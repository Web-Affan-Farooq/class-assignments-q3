class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print("Car started ...")

car1 = Car('Suzuki')
print(f"Brand is : {car1.brand}")
car1.start()