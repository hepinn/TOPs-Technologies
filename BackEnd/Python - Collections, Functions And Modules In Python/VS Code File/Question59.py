#Write a Python program to convert degree to radian

import math

def deg_to_rad(deg):
    rad = deg * (math.pi / 180)
    return rad

deg = float(input("Enter a degree value: "))
rad = deg_to_rad(deg)
print(deg,"degrees is equal to",rad,"radians")