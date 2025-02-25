import os
from typing import Tuple, Union

class FormulaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def parse_equation(equation: str) -> Tuple[float, str, float]:
    """Parse and validate the input equation."""
    if " " in equation:
        parts = equation.strip().split()
    else:
        parts=[]
        for i in equation:
            parts.append(i)
    
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        raise FormulaError("❌ Please enter valid numbers!")
    
    if operator not in ['+', '-']:
        raise FormulaError("❌ Invalid operator! Please use + or -")
        
    return num1, operator, num2

def calculate(num1: float, operator: str, num2: float) -> float:
    """Perform the calculation."""
    if operator == '+':
        return num1 + num2
    return num1 - num2

def format_result(result: float) -> str:
    """Format the result to remove unnecessary decimal places."""
    return str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result)

def display_help():
    """Display help information."""
    print("\n📖 Calculator Help:")
    print("• Enter calculations in the format: number operator number")
    print("• Example: 5 + 3 or 10.5 - 2.5")
    print("• Supported operators: + and -")
    print("• Type 'quit' to exit")
    print("• Type 'help' for this information")
    print("• Type 'clear' to clear the screen\n")

def main():
    clear_screen()
    print("\n🧮 Welcome to the Simple Calculator! 🧮")
    display_help()

    while True:
        try:
            # Get user input
            print("\n➡️  Enter calculation (or help/quit/clear):")
            equation = input("    ").lower()
            
            # Handle special commands
            if equation == 'quit':
                print("\n👋 Thanks for using the calculator! Goodbye!\n")
                break
            elif equation == 'help':
                display_help()
                continue
            elif equation == 'clear':
                clear_screen()
                continue
            elif not equation.strip():
                print("❌ Please enter a calculation!")
                continue
                
            # Parse and calculate
            num1, operator, num2 = parse_equation(equation)
            result = calculate(num1, operator, num2)
            
            # Display result with appropriate formatting
            formatted_result = format_result(result)
            print(f"\n✨ Result: {num1} {operator} {num2} = {formatted_result}")
            
        except FormulaError as e:
            print(f"\n{e}")
            print("💡 Type 'help' for usage instructions")
        except KeyboardInterrupt:
            print("\n\n👋 Calculator interrupted. Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {str(e)}")
            print("💡 Type 'help' for usage instructions")

if __name__ == '__main__':
    main()