"""
Functions:
- is_different(nums): Determines if a list contains only unique elements.
"""

def is_different(nums):
    """
    Check if all elements in the given list are unique.

    Parameters:
    nums (list): The list of numbers to check.

    Returns:
    bool: True if all elements are unique, False otherwise.
    """
    # Convert the list to a set and compare lengths
    if len(nums) == len(set(nums)):
        return True
    return False


# Take user input and split it into a list
nums = [i for i in input("Enter numbers separated by spaces: ").split()]

# Check if all elements are unique and print the result
print(is_different(nums))
