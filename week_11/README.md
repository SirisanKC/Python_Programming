# Python Programming - Week 11 Tasks

This week emphasizes working with **tuples**, **pairs from lists**, and **NumPy matrices**, including creation, manipulation, sorting, reshaping, and calculations.

---

## 📌 Tasks Overview

### ✅ L11-T1: Tuple — Powers of a Number
- Implement a function `powers(x)` that returns a **tuple** containing x², x³, x⁴, and x⁵.
- Round and print each result to 4 decimal places.

**Sample Output:**
```

Enter a number:
56.2
Powers of 56.2:
x^2: 3158.44
x^3: 177504.328
x^4: 9975743.2336
x^5: 560636769.7283

```

---

### ✅ L11-T2: Potential Pairs of Elements
- Accept a list of integers from the user.
- Stop collecting when the user types `'done'`.
- Ask for a **target sum**, and display all valid (x, y) pairs where `x + y = target` and `x <= y`.
- Handle invalid inputs gracefully.

**Sample Output:**
```

Enter the target sum:
7
Pairs with a sum of 7:
(1, 6)
(2, 5)
(3, 4)

```

---

### ✅ L11-T3: Matrix 1 (Using NumPy)
- Ask for dimensions and content of two matrices.
- Create NumPy arrays from input.
- Perform and display:
  - **Sum** (if compatible).
  - **Matrix multiplication** (if compatible).
- Show error messages when operations are not possible.

**Sample Output:**
```

Matrix sum:
\[\[6. 8.]
\[10. 12.]]
Matrix multiplication:
\[\[19. 22.]
\[43. 50.]]

```

---

### ✅ L11-T4: Matrix 2 (Advanced NumPy)
- Steps:
  1. Create a zero matrix using `np.zeros()`.
  2. Fill matrix using formula `(row+1)*(column+1)`.
  3. Print matrix using NumPy format.
  4. Flatten and sort the matrix using `np.sort()`.
  5. Print sorted matrix using semicolon-separated formatting.
  6. Allow reshaping with error handling for incompatible dimensions.
  7. Compute:
     - Max value
     - Min value
     - Sum of all values
  8. Ask for list of integers from user, remove duplicates using NumPy, and sort.

**Sample Output:**
```

Zero-matrix of the given rows & columns is:
\[\[0 0 0 0]
\[0 0 0 0]
\[0 0 0 0]
\[0 0 0 0]]

Matrix printed with np-formatting:
\[\[ 1  2  3  4]
\[ 2  4  6  8]
\[ 3  6  9 12]
\[ 4  8 12 16]]

Matrix sorted into one array:
\[1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16]

Matrix printed with elements separated by semicolons:
1;2;3;4;
2;4;6;8;
3;6;9;12;
4;8;12;16;

Newly shaped matrix is:
\[\[ 1  2  3  4  2  4  6  8]
\[ 3  6  9 12  4  8 12 16]]

Largest number in the matrix is: 16
Smallest number in the matrix is: 1
Sum of all values in the matrix is: 100

Unique values are: \[ 3  4  5 11 12 13 15 16 18 22 32 34 44 55]

```

## ⚠️ Notes

- Follow output formatting and rounding exactly.
- Handle invalid user inputs gracefully.
- "Code Structure Tests" will validate your function names and return types.

---

## 📚 Libraries Used

- `math` (for power calculations)
- `NumPy` (for matrix manipulation and sorting)

---

## 📄 License

This project is for **educational use only** as part of the Python Programming course curriculum.
```

---

Let me know if you'd like this compiled together with previous README files into a zip or GitHub-style documentation.

