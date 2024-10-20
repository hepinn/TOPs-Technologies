'''Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd
'''

import itertools

def combine_letters(dictionary):
    letter_lists = list(dictionary.values())

    combinations = itertools.product(*letter_lists)

    for combination in combinations:
        print(''.join(combination))

data = {'1': ['a', 'b'], '2': ['c', 'd']}

combine_letters(data)