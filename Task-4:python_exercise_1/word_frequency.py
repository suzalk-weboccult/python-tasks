"""
This module provides functionality to count the frequency of words in a given text.

Functions:
- count_word_frequencies(text): Parses a given text and returns a dictionary with word counts.
"""

import re

def count_word_frequencies(text):
    """
    Count the frequency of words in the given text.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary where keys are words and values are their corresponding frequencies.
    """
    res = {}  # Dictionary to store word frequencies

    # Extract words from the text while considering apostrophes in contractions
    words = re.findall(r"\b\w+(?:'\w+)?\b", text, re.UNICODE)

    # Count the occurrences of each word
    for word in words:
        res[word] = res.get(word, 0) + 1

    return res

# Take user input for the text
text = input("Enter the text: ")

# Count word frequencies and print the result
print(count_word_frequencies(text))