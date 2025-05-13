def input_integer():
    try:
        return int(input("Enter an integer:\n"))

    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def main():
    givenInteger = input_integer()
    
    print(f"Now give {givenInteger} integers!")

    sum= 0
    count = 0

    while count < givenInteger:
        value = input_integer()

        if value is None:
            continue

        sum += value
        count += 1

    print(f"The sum of the entered integers is: {sum}")

    

main()