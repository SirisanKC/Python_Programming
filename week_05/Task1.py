def printFun():
    print("Function 1:\nThis is printed in the function")
    
    
def num():
    print("\nFunction 2:")
    x = int(input("Enter a number:\n"))
    print(f"The input number is {x}")
    print(f"The number square is {x**2}")
    
def name():
    print("\nFunction 3:")
    fName = input("Enter your first name:\n")
    lName = input("Enter your last name:\n")
    print(f"The full name is {fName} {lName}")
    
    
    
printFun()
num()
name()