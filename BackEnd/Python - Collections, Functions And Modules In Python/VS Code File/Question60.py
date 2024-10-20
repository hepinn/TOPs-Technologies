#Write a Python program to calculate the area of a trapezoid

def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

a = 5
b = 10
h = 6

area = trapezoid_area(a, b, h)
print("The area of the trapezoid is",area,"square units.")