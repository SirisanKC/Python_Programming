def main():
    try:
        num1 = input("Enter the first number:\n")
        num2 = input("Enter the second number:\n")

        num1 = float(num1)
        num2 = float(num2)

        result = num1/num2

        print(f"The result of {num1} / {num2} is {result:.8f}")

    except ValueError:
        print("You must enter valid numbers")

    except ZeroDivisionError:
        print("You cannot divide by zero")

main()