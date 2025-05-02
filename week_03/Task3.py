first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))


print("The calculator can perform the following operations:")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")


print(f"The numbers you entered are {first_number} and {second_number}")


operation = int(input("Select the operation (1-4):\n"))


if operation == 1:
    result = first_number + second_number
    print(f"Selection 1: {first_number} + {second_number} = {result}")
elif operation == 2:
    result = first_number - second_number
    print(f"Selection 2: {first_number} - {second_number} = {result}")
elif operation == 3:
    result = first_number * second_number
    print(f"Selection 3: {first_number} * {second_number} = {result}")
elif operation == 4:
    if second_number == 0:
        print("Error: Zero cannot be used as a divisor.")
    else:
        result = round(first_number / second_number, 2)
        print(f"Selection 4: {first_number} / {second_number} = {result}")
else:
    print("The operation was not recognized.")
