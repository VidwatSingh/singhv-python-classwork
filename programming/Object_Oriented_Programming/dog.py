class Dog:
    def __init__(self, myName, myColour) -> None:
        self.name = myName
        self.colour = myColour
    #end procedure
    def bark(self, bark_times):
        for _ in range (bark_times):
            print("Woof!")
        #end for loop
    #end method
    def setColour(self, colour):
        self.colour = colour
    #end method
    def getColour(self):
        return self.colour
    #end procedure

#end class

my_dog = Dog("Fido", "Black")
my_dog.bark(2)
print(my_dog.name)
my_dog.bark(3)
my_dog.setColour("red")
print(my_dog.getColour("red"))