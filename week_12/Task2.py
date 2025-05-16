def sum_of_digits_recursive(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_recursive(n // 10)


n = 1234
print(f"Sum of digits of {n} is {sum_of_digits_recursive(n)}")
