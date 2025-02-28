import re

def is_first_word_vowel(lst):
    """
    Filters words from the given list that start with a vowel (A, E, I, O, U).

    Parameters:
    lst (list of str): A list of words.

    Returns:
    list of str: A list containing only words that start with a vowel.
    """
    res = []
    for word in lst:
        # Check if the first character of the word is a vowel (case-insensitive)
        if word[0] in "aeiouAEIOU":
            res.append(word)
    return res

# Take user input and extract words using regex
words = input("Enter the words in the list: ")
words = re.findall(r"\b\w+'?\w*|\w+", words)  # Extract words, keeping contractions like "it's"

# Call the function and print the filtered list
print(is_first_word_vowel(words))