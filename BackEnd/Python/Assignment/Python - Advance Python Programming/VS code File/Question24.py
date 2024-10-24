# Q.24 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math

class Circle:
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    circle = Circle(5)    
    print(f"The area of the circle is: {circle.area():.2f}")  # Output: Area
    print(f"The perimeter of the circle is: {circle.perimeter():.2f}")  # Output: Perimeter
