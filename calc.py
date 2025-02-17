
class FormulaError(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message})"

def main():

    while True:
        eq=input()

        if eq=="quit":
            break

        lst=eq.split()
        
        if len(lst)!=3:
            raise FormulaError("invalid length of equation.")

        try:
            lst[0]=float(lst[0])
            lst[2]=float(lst[2])

        except ValueError:
            raise FormulaError("error occured in converting string to float")

        if lst[1]=='+' or lst[1]=='-':
            print(eval(eq))
        else:
            raise FormulaError("operator is invalid")
    

if __name__ == '__main__':
    main()