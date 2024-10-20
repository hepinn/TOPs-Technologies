#Write a Python program to calculate the area of a parallelogram

def calculate_parallelogram_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    area = base * height
    return area

base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

try:
    area = calculate_parallelogram_area(base, height)
    print(f"The area of the parallelogram is",area,"square units.")
except ValueError as e:
    print(e)