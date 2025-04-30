'''
Attributs / properties are variables inside of a class.
Methods are functions inside of a class.
'''

# BASE CLASS ( PARENT CLASS / SUPERCLASS )
class Animal:
    # To run this method and create an instance of this class, you must type the name of the class, followed by (). Ex: Animal()
    def __init__(self, name):
        self.name = name
        self.living = True
        self.legCount = 4
        self.location = "Home"
        print(self.name + " has been created.")
    
    def walk(self, destination):
        self.location = destination
        print(f"{self.name} walks to {self.location}.")
  
# SUBCLASSES (CHILD CLASSES) -- These inherit from the parent class Animal. They 'extend' Animal.
class Dog(Animal):
    def bark(self, target):
        print(f"{self.name} is barking at {target}.")

class Cat(Animal):
    def highjump(self, target):
        print(f"{self.name} does a very high jump onto {target}.")

'''
INSTANTIATING THE ANIMAL CLASSES & ACCESSING ITS PROPERTIES / METHODS
'''
print("\nINSTANTIATING THE ANIMAL CLASSES & ACCESSING ITS PROPERTIES / METHODS:")
animal1 = Animal("Fluffy")
animal2 = Animal("Peanut")

animal1.walk("the dog park")
animal2.walk("the forest")

print(animal1.location)
print(animal2.location)

'''
INSTANTIATING THE SUBCLASSES & ACCESSING THEIR PROPERTIES / METHODS
'''
print("\nINSTANTIATING THE SUBCLASSES & ACCESSING THEIR PROPERTIES / METHODS:")
dog1 = Dog("Shadow")
dog1.walk("the dog park")
dog1.bark("the other dogs")

cat1 = Cat("Monster")
cat1.walk("the food bowl")
cat1.highjump("the kitchen counter")