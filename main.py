
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


#
# class Car:
#     def __int__(self, year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model
#         self.runnning = False
#         self.speed = 0
#
#     def turnOn(self):
#         self.running = True
#         print(f"the car is now {self.running}")
#
#     def turnOff(self):
#         self.running = False
#         print(f"the car is now {self.running}")
#
#     def changeSpeed(self, accel):
#         self.speed += accel
#         print(f"the car's speed is now {self.speed}")
#
#
#
# car1 = Car(2018, "Ford", "Mustang")
# car2 = Car(1962, "Ford", "Mustang")
# car3 = Car(2016, "Ford", "Mustang")

#
# class Character:
#     def __init__(self, name, phrase1, phrase2):
#         self.name = name
#         self.phrase1 = phrase1
#         self.phrase2 = phrase2
#         self.level = 0
#
#
#     def speak(self, phraseNum):
#         if phraseNum == 1:
#             print(self.phrase1)
#         elif phraseNum == 2:
#             print(self.phrase2)
#         else:
#             print("not valid phrase number")
#     def setLevel(self, newLevel):
#         self.level = newLevel
#         print(f"New level of is now {self.level}")
#
#
#
#
#
# stalin_quote_1 = "Those who vote decide nothing. Those who count the vote decide everything."
# stalin_quote_2 = "The only real power comes out of a long rifle."
# Stalin = Character("Stalin", stalin_quote_1, stalin_quote_2)
#
# churchil_quote_1 = "Success consists of going from failure to failure without loss of enthusiasm."
# churchil_quote_2 = "The best argument against democracy is a five-minute conversation with the average voter."
# Churchil = Character("Churchil", churchil_quote_1, churchil_quote_2)
#
#
# Character.speak(Stalin, 1)
# Character.setLevel(Stalin, 2)
# Character.speak(Churchil, 2)

class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    def openBag(self):
        self.open = True
        print("The bag is now Open")

    def closeBag(self):
        self.open = False
        print("The bag is now Closed")

    def putin(self, item):
        if self.open:
            self.items.append(item)
            print(f"{item} has been added to the bag")
        else:
            print("The bag is not Open")
    def takeOut(self, item):
        if self.open:
            self.items.remove(item)
            print(f"{item} has been removed from the bag")
        else:
            print("The bag is not Open")


blue = Backpack("small", "Blue")
red = Backpack("median", "Red")
green = Backpack("large", "Green")

Backpack.openBag(blue)
Backpack.putin(blue, "lunch")
Backpack.putin(blue, "Jacket")
Backpack.closeBag(blue)
Backpack.openBag(blue)
Backpack.takeOut(blue,"lunch")
Backpack.closeBag(blue)








