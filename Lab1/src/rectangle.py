"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def set_values(self, x, y):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.__width = None
        self.__height = None
        
    def set_values(self, x, y):
        self.__width = x
        self.__height = y

    def area(self):
        return self.__width * self.__height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
