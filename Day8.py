class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print("\n🚗 Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

brand = input("Enter the car brand: ")
model = input("Enter the car model: ")
year = input("Enter the manufacturing year: ")
color = input("Enter the car color: ")

user_car = Car(brand, model, year, color)
user_car.display_info()

