"""
This module provides functions to compute the factorial of a number using both iterative
and recursive approaches.

Functions:
- factorial_any_number(num): Computes factorial
- fact_iterative(num): Computes factorial iteratively.
- fact_recursive(num): Computes factorial recursively.
"""
import math

def factorial_any_number(num):
    """
    Computes the factorial of any number, including non-integer values, using the Gamma function.

    The Gamma function generalizes the factorial function for real and complex numbers.
    For positive integers, Gamma(n) = (n-1)!.

    Parameters:
    num (float or int): The number for which the factorial is to be computed.

    Returns:
    float: The factorial of the given number.
    """
    return math.gamma(num + 1)  # Gamma(n+1) is equivalent to n!


def fact_iterative(num):
    """
    Calculate the factorial of a given number iteratively.

    Parameters:
    num (int): The number for which factorial is to be computed.

    Returns:
    int: The factorial of the given number.
    """
    # Loop through numbers from 2 to num-1 and multiply to get factorial
    for i in range(2, num):
        num = num * i
    return num

def fact_recursive(num):
    """
    Calculate the factorial of a given number recursively.

    Parameters:
    num (int): The number for which factorial is to be computed.

    Returns:
    int: The factorial of the given number.
    """
    # Base case: factorial of 0 or 1 is 1
    if num <= 1:
        return 1
    # Recursive case: num * factorial of (num-1)
    return num * fact_recursive(num - 1)

# Take user input for the number
number = input("Enter the positive number of which you want to calculate factorial: ")
while "-" in number:
  number = input("Enter the positive number of which you want to calculate factorial: ")

if "." in number:
  number=float(number)
  print("Factorial (decimal):",factorial_any_number(number))
else:
  number=int(number)
  # Print factorial using iterative and recursive methods
  print("Factorial (Iterative):", fact_iterative(number))
  print("Factorial (Recursive):", fact_recursive(number))
