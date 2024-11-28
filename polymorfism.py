class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name} . My age is {self.age}") 
    def make_sound(self):  
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name} . My age is {self.age}") 
    def make_sound(self):  
        print("woof")

Cat1 = Cat("Sam",12)
Dog1 = Dog("Jack",8)

for animal in (Dog1,Cat1):
    animal.info()
    animal.make_sound()

