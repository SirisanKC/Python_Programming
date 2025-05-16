import time

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


for n in [30, 35, 40]:
    start = time.time()
    result = Fibonacci(n)
    end = time.time()
    print(f"Fibonacci({n}) = {result}, computed in {end - start:.4f} seconds")
