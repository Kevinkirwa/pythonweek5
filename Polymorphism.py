# Base Class: Vehicle
class Vehicle:
    def move(self):
        pass  # Abstract method

# Derived Class: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Derived Class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴‍♂️"

# Testing Polymorphism
vehicles = [Car(), Plane(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())
