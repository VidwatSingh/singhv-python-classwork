class building:
    def __init__(self, pHeight, pWidth, pFloors) -> None:
        self.__height = pHeight # private
        self.__width = pWidth   # private
        self.__floor = pFloors  # private
    #end constructor (new)

    def getNumFloors(self):
        return self.__floor
    #end function

    def setNumFloors(self, pFloors):
        if pFloors >= 1:
            self.__floor = pFloors
            return True
        else:
            return False
        #end if
    #end function
#end class

class house (building):
    #attribute
    def __init__(self, pHeight, pWidth, pFloors, pBathrooms, pBedrooms) -> None:
        super().__init__(pHeight, pWidth, pFloors)
        self.__bathrooms = pBathrooms
        self.__bedrooms = pBedrooms
    #end contructor (new)
#end class

my_building = building(100, 50, 10)
print(my_building._building__height)