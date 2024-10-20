# Q.4 Write a python function to get the largest number, smallest num and sum of all from a list.

list1 = []
num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)


print("Largest element is:", max(list1))
print("Smallest element is:", min(list1))
print("Sum of all number",sum(list1))
