import math

def valueError():
    try:
        num = int(input("Give a non-negative integer: \n"))
        result = math.sqrt(num)
        print(f"Square root of {num} is {result:.2f}.")
    except ValueError:
        print("ValueError happened. Non-negative number expected for square root.")

def indexError():
    elements = [11, 22, 33, 44, 55]
    try:
        index = int(input("Input index 0-4: \n"))
        print(f"List value is {elements[index]} at index {index}.")
    except IndexError:
        print(f"Got an IndexError with index {index}.")

def zeroDivisionError():
    try:
        divider = int(input("Enter divider: \n"))
        result = 4 / divider
        print(f"4/{divider} = {result:.2f}.")
    except ZeroDivisionError:
        print(f"ZeroDivisionError occurred, divider {divider}.")

def typeError():
    try:
        number = input("Enter number:\n")
        result = number * number
        print(f"Result: {result}")
    except TypeError:
        print("Got TypeError. Two strings cannot be multiplied together.")

def main():
    while True:
        print("What do you want to do:")
        print("1) Test for ValueError")
        print("2) Test for IndexError")
        print("3) Test for ZeroDivisionError")
        print("4) Test for TypeError")
        print("0) Stop")
        while True:
            try:
                choice = int(input("Your choice:\n"))
                break
            except ValueError:
                print("ValueError happened. Enter the selection as an integer.")
        
        if choice == 1:
            valueError()
        elif choice == 2:
            indexError()
        elif choice == 3:
            zeroDivisionError()
        elif choice == 4:
            typeError()
        elif choice == 0:
            print("See you again!")
            break
        else:
            print("Unknown selection, please try again.")

main()