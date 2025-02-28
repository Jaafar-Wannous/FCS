class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Rental Price per Day: ${self.__rental_price_per_day}")
    
    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days
    
    def get_rental_price(self):
        return self.__rental_price_per_day
    
    def set_rental_price(self, price):
        if price > 0:
            self.__rental_price_per_day = price
        else:
            print("Invalid price!")
    

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Seating Capacity: {self.seating_capacity} seats")

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity} CC")

def show_vehicle_info(vehicle):
    vehicle.display_info()
    print("-")

car1 = Car("Toyota", "Corolla", 2022, 50, 5)
bike1 = Bike("Yamaha", "R3", 2021, 30, 321)

show_vehicle_info(car1)
show_vehicle_info(bike1)

days = 3
print(f"Rental cost for {days} days (Car): ${car1.calculate_rental_cost(days)}")
print(f"Rental cost for {days} days (Bike): ${bike1.calculate_rental_cost(days)}")

car1.set_rental_price(60)
bike1.set_rental_price(35)

print(f"Updated Car Rental Price: ${car1.get_rental_price()}")
print(f"Updated Bike Rental Price: ${bike1.get_rental_price()}")
