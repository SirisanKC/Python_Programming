
```markdown
# Python Programming - Week 12 Tasks (Recursion & Complexity)

This week's focus is on **recursive programming**, understanding **algorithmic complexity**, and **benchmarking sorting algorithms**. You'll build your own recursive solutions for summation and Fibonacci sequences, explore performance issues, and compare sorting strategies using real-time measurements.


---

## 📌 Tasks Overview

### ✅ L13-T1: Recursion — Sum of List
- Implement: `sum_of_list_recursive(numbers)`
- Recursively sum all elements in a list of integers or floats.
- Include a simple `main()` program to demonstrate the function.

---

### ✅ L13-T2: Recursion — Sum of Digits
- Implement: `sum_of_digits_recursive(n)`
- Return the sum of the digits of a non-negative integer `n`.
- Example: `123` → `1 + 2 + 3 = 6`

---

### ✅ L13-T3: Fibonacci Sequence
- Implement: `Fibonacci(n)`
- Use a **recursive** approach.
- Function returns the `n`th number in the Fibonacci sequence.
- Initial conditions:
  - `F(0) = 0`
  - `F(1) = 1`

---

### ✅ L13-T4: Complexity Issues with Recursion
- Run your `Fibonacci(n)` function with large `n` values: 30, 35, 40, 45, ...
- Observe performance slowdowns.
- Explain **why** the function slows down — e.g., exponential growth of recursive calls, redundant calculations.

---

### ✅ L13-T5: Improved Fibonacci (Linear Time)
- Write an optimized Fibonacci version with **linear time complexity**.
- Use **memoization** or **iterative implementation**.
- Function signature: `Fibonacci_improved(n)`

---

### 🧪 EXTRA: Benchmark Sorting Algorithms
Use the file `pseudo_words.txt` (100,000 words of length 8) from Moodle.

1. `read_words(file_name)` — Reads and returns a list of words.
2. Create **three deep copies** of this list using `copy.deepcopy()`.
3. Implement or use the following sorting methods:
   - `sorted()` (built-in)
   - `quicksort()` (from lectures)
   - `insertionSort()` (from lectures)
4. Measure their execution times using the `time` module.

**Sample Output:**
```

Time taken by sorted(): 0.126543 seconds
Time taken by quicksort(): 0.298274 seconds
Time taken by insertionSort(): 24.932318 seconds

```

---

## 📝 Notes

- All tasks require **a main program** to demonstrate each function.
- These exercises reinforce understanding of **recursion, complexity, and performance analysis**.
- For sorting, ensure lists are not mixed by using `deepcopy()`.

---

## 🔧 Concepts Practiced

- Recursive function design
- Base cases and recursive cases
- Exponential vs linear time complexity
- Memoization
- Sorting algorithm benchmarking

---

## 📚 Libraries Used

- `copy` (for `deepcopy`)
- `time` (for benchmarking)
- Standard Python list and recursion techniques

---

## 📄 License

This project is for **educational purposes only** as part of the Python Programming course.
```

---

Would you like a zip file with Python code templates and all README files included for submission or archiving?

