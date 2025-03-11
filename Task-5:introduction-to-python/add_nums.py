"""
This module provides a function to add two numbers and return their sum.
"""

def add_nums(a: int, b: int) -> int:
    """
    Adds two numbers and returns the sum.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    lst = []  # Initialize an empty list
    lst.append(a)  # Append first number
    lst.append(b)  # Append second number
    return sum(lst)  # Return the sum of the list


def main():
    """Main function to take user input and print the sum."""
    try:
        a = float(input("Enter first number: "))  # Take first number input
        b = float(input("Enter second number: "))  # Take second number input
        print("Sum of two numbers:", add_nums(a, b))  # Print the sum
    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()
