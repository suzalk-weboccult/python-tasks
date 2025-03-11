"""Module to classify numbers as odd or even."""

# Lambda function to check if a number is odd or even
check_odd_even_num = lambda x: "Even" if x % 2 == 0 else "Odd"

def main():
    """Main function to take user input and classify numbers as odd or even."""
    while True:
        try:
            # Take comma-separated integer input from the user
            nums = list(map(int, input("Enter numbers separated by commas: ").split(",")))
            
            even_nums = []  # List to store even numbers
            odd_nums = []   # List to store odd numbers
            
            # Classify numbers as even or odd
            for num in nums:
                if check_odd_even_num(num) == "Even":
                    even_nums.append(num)
                else:
                    odd_nums.append(num)
            
            # Print classified numbers
            print("Even numbers:", even_nums)
            print("Odd numbers:", odd_nums)
            return
        except ValueError:
            # Handle invalid input error
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()