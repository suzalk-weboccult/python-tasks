import random

class InvalidInputError(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message})"

while True:
    num=random.randrange(1,10)
    attempts=0

    while True:
        guess_num=int(input())

        if attempts==5:
            print(f"you have taken many attempts. you are having only 5 attempts max to get the number right.")
            choice=int(input("please enter 1 for play again or 2 for exit"))
            if choice==1:
                print(f"you have taken {attempts} attempts before guessing the right number")
                break
            else:
                print(f"you have taken {attempts} attempts before guessing the right number")
                exit()


        if guess_num not in range(1,10):
            raise InvalidInputError("please enter the number in range 1 to 10 only")

        if guess_num==num:
            choice=int(input("please enter 1 for play again or 2 for exit"))
            if choice==1:
                print(f"you have taken {attempts} attempts before guessing the right number")
                break
            else:
                print(f"you have taken {attempts} attempts before guessing the right number")
                exit()
        else:
            attempts+=1