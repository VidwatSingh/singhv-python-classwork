class Animal:
    def __init__(self, type, name, colour) -> None:
        self.type = type
        self.name = name
        self.colour = colour
    #end constructor method 

    def eat(self):
        pass
    #end public procedure

    def make_noise(self):
        pass
    #end public procedure

    def move(self):
        pass
    #end public procedure

#end class

my_animal = Animal("Unknown", "Adam", "Yellow")
print(f"type: {my_animal.type}, name: {my_animal.name}, colour: {my_animal.colour}")
my_animal.make_noise()
print("End")

class Dog(Animal):
    def make_noise(self):
        print("woof")
    #end public procedure
#end class

my_dog = Dog("Mammal", "Fido", "Black")
print(f"type: {my_dog.type}, name: {my_dog.name}, colour: {my_dog.colour}")
print("End")
my_dog.make_noise()


class cat(Animal):
    def make_noise(self):
        print("meow")
    #end public procedure
#end class

my_cat = cat("Mammal", "Yoruichii", "Brown")
print(f"type: {my_cat.type}, name: {my_cat.name}, colour: {my_cat.colour}")
print("End")
my_cat.make_noise()


animals = []
for animal in ['cat', 'dog', 'dog', 'cat', 'cat']:
    match animal:
        case 'cat':
            animals.append(cat("Mammal", "Yoruichii", "Brown"))
        case 'dog':
            animals.append(Dog("Mammal", "Fido", "Black"))
    #end match
#next animal

for animal in animals:
    animal.make_noise()
#next animal