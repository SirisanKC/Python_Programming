print("This program calculates the average of the 3 numbers you enter.")
print("The numbers can be int's or float's.")

fNum = float(input("Enter the first number:\n"))
sNum = float(input("Enter the second number:\n"))
tNum = float(input("Enter the third number:\n"))

print(f"Sum of the numbers: {fNum+sNum+tNum}")
print(f"Average of the numbers (rounded to 3 decimal places): {(fNum+sNum+tNum)/3:.3f}")
print(f"Average of the numbers (rounded to the closest integer): {round((fNum+sNum+tNum)/3)}")
print(f"Average of the numbers as an integer without the decimal part: {int((fNum+sNum+tNum)/3)}")