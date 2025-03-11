"""
This module provides a function to check if a list contains only unique elements.
"""

def is_different(nums: list) -> bool:
    """
    Check if all elements in the given list are unique.

    Args:
        nums (list): The list of numbers to check.

    Returns:
        bool: True if all elements are unique, False otherwise.
    """
    return len(nums) == len(set(nums))  # Convert the list to a set and compare lengths


def get_user_input() -> list:
    """Prompt the user for a list of numbers and return them as a list."""
    while True:
        try:
            nums = list(map(int, input("Enter numbers separated by comma: ").split(",")))
            return nums
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def main():
    """Main function to take user input and check for unique numbers."""
    nums = get_user_input()
    if is_different(nums):
        print("All numbers are different.")
    else:
        print("There are duplicate numbers.")


if __name__ == "__main__":
    main()
