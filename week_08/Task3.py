from fractions import Fraction

def main():
    print("Give the first fraction.")

    num1 = int(input("Give numerator (top):\n"))
    den1 = int(input("Give denominator (bottom):\n"))

    print("Give the second fraction.")

    num2 = int(input("Give numerator (top):\n"))
    den2 = int(input("Give denominator (bottom):\n"))

    expo= int(input("Give an exponent:\n"))


    fraction1 = Fraction(num1, den1)
    fraction2 = Fraction(num2, den2)

    sum_result = fraction1 + fraction2
    subtract_result = fraction1 - fraction2
    multiply_result = fraction1 * fraction2
    divide_result = fraction1 / fraction2
    power_result = fraction1 ** expo

    print(f"Sum: {fraction1} + {fraction2} = {sum_result}")
    print(f"Subtract: {fraction1} - {fraction2} = {subtract_result}")
    print(f"Multiply: ({fraction1}) * ({fraction2}) = {multiply_result}")
    print(f"Divide: ({fraction1}) / ({fraction2}) = {divide_result}")
    print(f"Power: ({fraction1})**{expo} = {power_result}")
    


main()