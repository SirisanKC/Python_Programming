def menu():
    print("Select one of the following operations:\n1) Enter integers\n2) Sum\n3) Subtract\n4) Multiplication\n5) Division\n0) Stop")
    return int(input("Select the function (0-5):\n"))

def enter_integer(text):
    return int(input(text))

def sum(value1,value2):
    result = value1 + value2
    return f"Sum {value1} + {value2} = {result}"

def subtract(value1,value2):
    result = value1 - value2
    return f"Subtract {value1} - {value2} = {result}"

def multiplication(value1,value2):
    result = value1 * value2
    return f"Multiplication {value1} * {value2} = {result}"

def division(value1,value2):
    if value2 == 0:
        return "You cannot divide by zero."
    else:
        result = round(value1 / value2, 2)
        return f"Division {value1} / {value2} = {result}"

def main():
    value1 = None
    value2 = None

    while True:
        choice = menu()

        if choice == 0:
            print("Bye.")
            break

        elif choice == 1:
            value1 = enter_integer("Enter first integer: \n")
            value2 = enter_integer("Enter second integer: \n")
            print(f"You inputted integers {value1} and {value2}")

        elif choice == 2 and value1 is not None and value2 is not None:
            print(sum(value1, value2))

        elif choice == 3 and value1 is not None and value2 is not None:
            print(subtract(value1, value2))

        elif choice == 4 and value1 is not None and value2 is not None:
            print(multiplication(value1, value2))

        elif choice == 5 and value1 is not None and value2 is not None:
            print(division(value1, value2))

        else:
            print("Unknown choice, try again.")
                

main()
