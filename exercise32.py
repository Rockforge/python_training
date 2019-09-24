# exercise32.py
# Classes


# Array is a list of 1 data types
# List allows multiple data types

# There is no private method in python
class Animal:

    # self is always required as first parameter

    # This is a dunder
    def __init__(self):
        pass
        # print('Animal created')

    def speak(self):
        print('Animal speaks')

# Inherits Animal class
class Dog(Animal):
    def __init__(self):
        self.name = 'Doggo'

    def speak(self):
        # Call the parent class and invoke the method
        super().speak()
        print("{} says bark".format(self.name))

class Corgi(Dog):
    def __init__(self, name):
        self.name = name

class Fox(Dog):
    def speak(self):
        print('ting a ding ding ding')

    def _dance(self):
        pass

zoo = [Animal(), Dog(), Corgi('Channy'), Fox()]

for animal in zoo:
    animal.speak()


# animal = Animal()
# animal.speak()

# animal2 = Dog()
# animal2.speak()