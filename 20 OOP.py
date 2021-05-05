class Vehicle:
    # Class attributes
    color = "White"
    def __init__(self, name, max_speed, mileage):
        # setting instance variables
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_instances(self):
        #self.welcome()
        print(f"Color: {self.color}, name is {self.name}, max speed is {self.max_speed}, mileage is {self.mileage}")

    def welcome(self):
        print("Welcome here")

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} vehicle is {capacity} passengers"

    def fare(self):
        return self.mileage * 100


class Bus(Vehicle):
    # Overriding method
    def seating_capacity(self, capacity=50):
        #return f"The seating capacity of a {self.name} bus is {capacity} passengers"
        return super().seating_capacity(capacity)

    def fare(self):
        amount = super().fare()
        return amount + amount * 10/100



modelx = Vehicle("Toyota", 200, 20)
modelx.print_instances()



volvog1 = Bus("Syamoli", 120, 15)
volvog1.print_instances()
print(volvog1.seating_capacity())
print("Total Bus fare is: ", volvog1.fare())

# Determine which class a given Bus object belongs to
print(type(volvog1))
# Determine if volvog1 is also an instance of the Vehicle class
print(isinstance(volvog1, Vehicle))
