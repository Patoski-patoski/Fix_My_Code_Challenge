#!/usr/bin/python3
"""Module documentation"""


class Square():
    """ A square class to get the area and perimeter"""

    width = 0
    height = 0
    
    def __init__(self, width=0, height=0):
        """Initialize instances
           Args:
                width: (Int) width
                height: (Int) height
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Calculate the area of the square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Calculate the permiter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=5, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
