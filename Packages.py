# 1)Create Main class to Inherit from
class MathFunctions:
    def __init__(self, addition, subtraction, multiplication, division):
        self.addition = addition
        self.subtraction = subtraction
        self.multiplication = multiplication
        self.division = division

# 2)Create a function for Inherited Class
    def task(self):
        a = int(input("Enter a Number: "))
        b = int(input("Enter another Number: "))
        total = (a + b) or (a - b) or (a * b) or (a / b)

        if total == (a + b):
            print(f"The added result is: {total}")
        elif total == (a - b):
            print(f"The subtracted result is: {total}")
        elif total == (a * b):
            print(f"The multiplied result is: {total}")
        elif total == (a / b):
            print(f"The divided result is: {total}")
        else:
            print("You have not entered any numbers to process")


# 3)Inherit from Main class
class Addition(MathFunctions):
    pass


class Subtraction(MathFunctions):
    pass


class Multiplication(MathFunctions):
    pass


class Division(MathFunctions):
    pass


# 4)Call function












