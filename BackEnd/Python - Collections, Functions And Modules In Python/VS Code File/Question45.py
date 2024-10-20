#Write a Python program to find the highest 3 values in a dictionary

my_dict = {"A": 3, "B": 4, "H": 1, "K": 8, "L": 2, "M": 9, "N": 7, "O": 6, "P": 5}

sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

top_3 = sorted_dict[:3]

result_dict = dict(top_3)

print(result_dict)