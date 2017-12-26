"""
Author: Ken Lambert
Demonstrates a function that traps number format errors during input.
"""
def safeIntegerInput(prompt):
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print("error in number format:", inputString)
        return safeIntegerInput(prompt)

if __name__ == '__main__':
    age = safeIntegerInput("Enter your age:")
    print("Your age is", age)
