class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Info: {self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

brand = input("Enter the car brand: ")
model = input("Enter the car model: ")
battery_capacity = input("Enter battery capacity (in kWh): ")

               #Creating ElectricCar object
my_electric_car = ElectricCar(brand, model, battery_capacity)

 #Displaying info
my_electric_car.display_info()
