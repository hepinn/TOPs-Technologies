#Write a Python program to returns sum of all divisors of a number

num = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, num + 1):
    if num % i == 0:
        sum_of_divisors += i
print("Sum of divisors:", sum_of_divisors)