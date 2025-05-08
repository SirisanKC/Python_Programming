def larger_value(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
        return a
    elif b > a:
        print(f"{b} is greater than {a}")
        return b
    else:
        print("The integers are the same.")
        return a


x = int(input("Enter the first integer:\n"))
y = int(input("Enter the second integer:\n"))
result = larger_value(x, y)

z = int(input("Enter the integer that is subtracted from the larger:\n"))
new_result = result - z

_ = larger_value(min(x, y), new_result)
