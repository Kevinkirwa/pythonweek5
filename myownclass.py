# Base Class: Gadget
class Gadget:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        return f"Brand: {self.brand}, Price: ${self.price}"

# Derived Class: Smartphone
class Smartphone(Gadget):
    def __init__(self, brand, price, os, camera_quality):
        super().__init__(brand, price)
        self.os = os
        self.camera_quality = camera_quality

    def show_details(self):
        details = super().show_details()
        return f"{details}, OS: {self.os}, Camera: {self.camera_quality}MP"

# Derived Class: Laptop
class Laptop(Gadget):
    def __init__(self, brand, price, ram, processor):
        super().__init__(brand, price)
        self.ram = ram
        self.processor = processor

    def show_details(self):
        details = super().show_details()
        return f"{details}, RAM: {self.ram}GB, Processor: {self.processor}"

# Testing the Classes
smartphone = Smartphone("Apple", 999, "iOS", 48)
laptop = Laptop("Dell", 850, 16, "Intel i7")

print(smartphone.show_details())  # Polymorphism in action
print(laptop.show_details())      # Polymorphism in action
