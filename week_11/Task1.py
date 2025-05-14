def calculate(x):
    return (x ** 2, x ** 3, x ** 4, x ** 5)

def main():
    x = float(input("Enter a number:\n"))

    result  = calculate(x)

    print(f"Powers of {x}:")
    print(f"x^2: {round(result[0], 4)}")
    print(f"x^3: {round(result[1], 4)}")
    print(f"x^4: {round(result[2], 4)}")
    print(f"x^5: {round(result[3], 4)}")

main()