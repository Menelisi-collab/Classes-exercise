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

