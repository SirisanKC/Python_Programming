def Fibonacci_improved(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


for i in range(10):
    print(f"Fibonacci_improved({i}) = {Fibonacci_improved(i)}")
