# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves in some way.")

# Subclasses with different move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the sea ")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
