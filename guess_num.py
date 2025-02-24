import random
import os

class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_number(prompt, min_val, max_val):
    """Get a valid number input from the user."""
    while True:
        try:
            user_input = input(prompt)
            num = int(user_input)
            if num < min_val or num > max_val:
                print(f"\n❌ Please enter a number between {min_val} and {max_val}")
                continue
            return num
        except ValueError:
            print("\n❌ Please enter a valid number!")

def play_game():
    """Main game function."""
    MAX_ATTEMPTS = 5
    number_range = (1, 10)
    secret_number = random.randrange(*number_range)
    attempts = 0
    
    # Welcome message
    clear_screen()
    print("\n🎮 Welcome to the Number Guessing Game! 🎮")
    print(f"\nI'm thinking of a number between {number_range[0]} and {number_range[1]}")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.")
    
    while attempts < MAX_ATTEMPTS:
        remaining_attempts = MAX_ATTEMPTS - attempts
        print(f"\nAttempts remaining: {remaining_attempts}")
        
        guess = get_valid_number(
            f"\nEnter your guess ({number_range[0]}-{number_range[1]}): ",
            number_range[0],
            number_range[1]
        )
        
        attempts += 1
        
        # Provide feedback
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You got it in {attempts} {'attempt' if attempts == 1 else 'attempts'}!")
            return True
        elif guess < secret_number:
            print("\n📈 Too low! Try a higher number.")
        else:
            print("\n📉 Too high! Try a lower number.")
        
        # Last attempt warning
        if attempts == MAX_ATTEMPTS - 1:
            print("\n⚠️ Warning: This is your last attempt!")
    
    print(f"\n😔 Game Over! The number was {secret_number}.")
    return False

def main():
    while True:
        play_game()
        
        # Ask to play again
        print("\nWould you like to play again?")
        print("1. Yes 🎮")
        print("2. No 👋")
        
        choice = get_valid_number("\nEnter your choice (1-2): ", 1, 2)
        
        if choice == 2:
            print("\n👋 Thanks for playing! Goodbye!\n")
            break
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}\n")