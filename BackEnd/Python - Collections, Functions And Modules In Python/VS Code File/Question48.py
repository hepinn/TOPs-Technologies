#Write a Python function to calculate the factorial of a number (a nonnegative integer)

n = int(input("Enter a nonnegative integer: "))

result = 1
for i in range(1, n + 1):
    result *= i

print("The factorial of",n,"is",result)