# Python Programming - Week 9 Tasks

This week's tasks focus on **exception handling** in Python, covering topics such as `None`, `try-except` with files, various built-in exceptions, and working with matrices safely.

---

## 📌 Tasks Overview

### ✅ L09-T1: `None` in Python
- Create a function `input_integer()` that uses a `try-except` block to handle non-integer input.
- Returns an integer or `None` if the input is invalid.
- Main program:
  - Ask user how many integers they want to input.
  - Use `input_integer()` repeatedly to collect them.
  - Skip `None` values and calculate the total sum.

**Example Output:**
```

Enter an integer:
4
Now give 4 integers!
Enter an integer:
1
Enter an integer:
g
Invalid input. Please enter an integer.
...
The sum of the entered integers is: 10

```

---

### ✅ L09-T2: File Read & Write with Exception Handling
- Implement two subroutines:
  - Read integers from a file into a list.
  - Write that list into another file.
- Use `try-except` in **each** function to catch file-related exceptions.
- Main program asks for file names and reports errors.

**Example Output:**
```

Enter the name of the file to be read:
T2\_file\_in1.txt
File 'T2\_file\_in1.txt' read successfully, 7 lines.
Enter the name of the file to be written:
T2\_file\_out.txt
File 'T2\_file\_out.txt' was successfully written.

```

---

### ✅ L09-T3: Exception Testing with Menu
- A menu-based program to test 4 exception types:
  1. `ValueError` — e.g., `math.sqrt(-1)`
  2. `IndexError` — invalid list access
  3. `ZeroDivisionError` — divide by zero
  4. `TypeError` — illegal type operation
- Each test has its own subroutine using only `try-except`, no `if` conditions.
- Handle incorrect menu input gracefully.

**Sample Menu:**
```

What do you want to do:

1. Test for ValueError
2. Test for IndexError
3. Test for ZeroDivisionError
4. Test for TypeError
5. Stop

```

---

### ✅ L09-T4: Multiple Exceptions with Division
- Prompt the user for two **float** numbers.
- Use `try-except` to handle:
  - `ValueError` — non-numeric input
  - `ZeroDivisionError` — division by 0
- Display result rounded to **8 decimal places**.

**Example Output:**
```

Enter the first number:
4.1
Enter the second number:
189.4
The result of 4.1 / 189.4 is 0.02164731

````

---

### ✅ L09-T5: Matrix Value Access
- Use a predefined matrix:
  ```python
  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]
````

* Ask the user for row and column indices.
* Use `try-except` to catch:

  * `IndexError` — out-of-bounds access
  * `ValueError` — invalid input (not integer)

**Example Output:**

```
Enter the row index:
3
Enter the column index:
1
Error: Index out of bounds. Please enter valid row and column indices.
```


## ⚠️ Notes

* Be careful with spacing and follow sample outputs strictly.
* Hidden "Code Structure Tests" will validate function names and structure compliance.
* Do not use `if` conditions where the task says to rely solely on `try-except`.

---

## 📚 Libraries Used

* `math`
* `os` (if used for file existence check)
* Basic Python exceptions (`ValueError`, `IndexError`, etc.)

---

## License

This repository is for **educational purposes only**.

```

---

Let me know if you'd like all weekly README files (L04–L09) compiled into a single document or repo format.
```
