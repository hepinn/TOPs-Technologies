#Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    return normalized_str == normalized_str[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("Hello, World!"))