class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping.")
    
Aardvark = Animal("Arthur")
GreenFrog = Frog("Kermit")

Aardvark.drink()
Aardvark.eat()


GreenFrog.drink()
GreenFrog.eat()
GreenFrog.jump()