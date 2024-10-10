# Q.17 Write a python program to get a single string two given strings, separated by a space and swap the first two character of each string.

def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz')) 
