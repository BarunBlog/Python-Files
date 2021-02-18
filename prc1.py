class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(f"Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # Overriding method
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


vehicle1 = Vehicle("Car", 200, 10)
vehicle1.print_vehicle()

bus1 = Bus("Volvo", 180, 12)
bus1.print_vehicle()
print(bus1.seating_capacity(51))
