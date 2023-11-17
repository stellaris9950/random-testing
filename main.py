
# # trying out this thing
# import random
# import math
#
#
# # Create a Circle class
# class Circle:
#     # Define constructor method with parameters
#     def __init__(self, initX, initY, initR):
#         # Add properties to empty self object
#         self.x = initX
#         self.y = initY
#         self.r = initR
#
#
#         print(f"New Circle Created: {self.x}, {self.y}, {self.r}")
#
#
#     # Methods (Functions / Behaviour)
#     def setCenter(self, newX, newY):
#         self.x = newX
#         self.y = newY
#         print(f"Center is now: ({self.x}, {self.y})")
#
#
#     def setRadius(self, newR):
#         self.r = newR
#         print(f"Radius is now: {self.r}")
#
#
#     def getArea(self):
#         return math.pi * (self.r ** 2)
#
#
#
#
# # Use Circle class to create two Circle objects
# # with the provided arguments.
# print("\nCIRCLE 1")
# circle1 = Circle(50, 100, 10)
# circle1.setCenter(500, 50)
# print(f"Circle 1's area is: {circle1.getArea()}.")
#
#
# print("\n CIRCLE 2")
# circle2 = Circle(200, 400, 100)
# print(f"Circle 2's area is: {circle2.getArea()}.")
# circle2.setRadius(10)
# print(f"Circle 2's area is: {circle2.getArea()}.")



class Car:
    def __int__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.runnning = False
        self.speed = 0

    def turnOn(self):
        self.running = True
        print(f"the car is now {self.running}")

    def turnOff(self):
        self.running = False
        print(f"the car is now {self.running}")

    def changeSpeed(self, accel):
        self.speed += accel
        print(f"the car's speed is now {self.speed}")



car1 = Car(2018, "Ford", "Mustang")
car2 = Car(1962, "Ford", "Mustang")
car3 = Car(2016, "Ford", "Mustang")













