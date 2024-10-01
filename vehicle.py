from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity  
        self.fuel_consumption = fuel_consumption 

    def drive(self, distance):
        pass

    def refuel(self, fuel):
        pass
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = self.fuel_consumption + 0.9
        needed_fuel = total_consumption * distance
        
        if needed_fuel > self.fuel_quantity:
            return "Not enough fuel to drive"
        
        self.fuel_quantity -= needed_fuel
        return f"Car drove {distance} km"

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel
        return f"Car refueled with {fuel} liters"    
from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = self.fuel_consumption + 1.6
        needed_fuel = total_consumption * distance
        
        if needed_fuel > self.fuel_quantity:
            return "Not enough fuel to drive"
        
        self.fuel_quantity -= needed_fuel
        return f"Truck drove {distance} km"

    def refuel(self, fuel):
        fuel_received = fuel * 0.95  
        self.fuel_quantity += fuel_received
        return f"Truck refueled with {fuel_received} liters (received {fuel} liters)"        
from car import Car
from truck import Truck

car = Car(fuel_quantity=50, fuel_consumption=5)  
print(car.drive(8))  
print(car.refuel(20))  
print(car.drive(10))  
truck = Truck(fuel_quantity=70, fuel_consumption=8)  
print(truck.drive(5))  
print(truck.refuel(30))  
print(truck.drive(10))          