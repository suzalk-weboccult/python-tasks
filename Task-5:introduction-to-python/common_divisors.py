"""Module to find common divisors of two numbers and display them."""

def common_divisors(a: int, b: int) -> list:
    """Finds and returns the common divisors of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        list: A list of common divisors of a and b.
    """
    divs = []  # List to store common divisors
    for i in range(1, min(a, b) + 1):  # Iterate up to the smaller number
        if a % i == 0 and b % i == 0:
            divs.append(i)  # Append to list if i is a common divisor
    return divs

def main():
    """Main function to take user input, find common divisors, and display them."""
    try:
        # Take integer input from user
        a = int(input("Enter first number (natural number): "))
        b = int(input("Enter second number (natural number): "))

        if a<1 or b<1:
            raise ValueError("Please enter natural numbers")

        # Get common divisors and print them
        divisors = common_divisors(a, b)
        print(f"Common divisors of {a} and {b} are: {divisors}")
    
    except ValueError:
        # Handle invalid input error
        print("Invalid input! Please enter natural numbers only.")

if __name__ == "__main__":
    main()