"""
This module provides a function to check whether a given string is a palindrome.

Functions:
- is_palindrome(s): Determines whether a string is a palindrome, ignoring punctuation and spaces.
"""

import string

def is_palindrome(s):
    """
    Check if a given string is a palindrome, ignoring punctuation and spaces.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Remove punctuation and spaces from the string
    s = s.translate(translator).replace(" ", "").lower()

    # Check if the cleaned string reads the same forward and backward
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

# Take user input for the string
st = input("Enter a string to check wether it is palindrome or not: ")

# Check and print whether the string is a palindrome
if is_palindrome(st):
    print(f"'{st}' is a palindrome")
else:
    print(f"'{st}' is not a palindrome")