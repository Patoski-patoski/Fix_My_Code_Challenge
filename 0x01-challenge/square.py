#!/usr/bin/python3

class Square():
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Calculate the area of the square"""
        return self.width * self.height

    def permeter_of_my_square(self):
        """Calculate the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square"""
        return "Square: {} x {}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=5, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
