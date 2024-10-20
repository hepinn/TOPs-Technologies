#Write a Python program to print all unique values in a dictionary.

data = [["name", "John"], ["age", 30], ["city", "New York"], ["name", "Alice"], ["age", 25], ["city", "Chicago"]]

unique_values = []

for item in data:
    if item[1] not in unique_values:
        unique_values.append(item[1])

print("Unique values:")
for value in unique_values:
    print(value)