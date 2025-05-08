# Python Programming - Week 6 Tasks

This week's tasks focus on **lists**, **matrices**, and **menu-based interactions** using Python functions and loops. You'll learn how to manipulate data structures and ensure user input validity.

---

## Tasks Overview

### ✅ L06-T1: Reversed List

- Implement a function that reverses a list of integers **without** using `reverse()` or slicing.
- Use the provided `input_integers()` function to collect input.

**Sample Output:**
```

Give integers separated by comma:
1,2,3,4,5
Reversed list: \[5, 4, 3, 2, 1]

```

---

### ✅ L06-T2: Remove Duplicates from List

- Implement a function that removes duplicate integers from a list while **preserving original order**.
- Use the provided `input_integers()` function.

**Sample Output:**
```

Give integers separated by comma:
3,2,3,1,6,2,3,4,5
Original List: \[3, 2, 3, 1, 6, 2, 3, 4, 5]
List with duplicates removed: \[3, 2, 1, 6, 4, 5]

```

---

### ✅ L06-T3: Shopping List Menu 

- Implement a menu-based shopping list app.
- Allow users to **add**, **remove**, or **end**.
- Use a function for menu handling.
- Print the list after every operation.

**Sample Output:**
```

Your shopping list contains the following products:
\['Milk', 'Tea']
You can choose from the functions below:

1. Add
2. Remove
3. End
   Your choice: 5
   Unknown selection.

```

---

### ✅ L06-T4: Matrix Creation and Printing 

- Create `create_matrix(rows, cols)` to collect user-entered matrix rows.
- Validate row length.
- Implement `print_matrix(matrix)` to print the matrix in a readable tab-separated format.

**Sample Output:**
```

Enter the number of rows: 2
Enter the number of columns: 3
Give row 1: 1 2
Error: Invalid number of elements in the row. Please try again.
Give row 1: 1 2 3
Give row 2: 4 5 6
|1	2	3|
|4	5	6|

```

---

### ✅ L06-T5: Matrix Transposition 

- Implement `transpose(matrix)` to return the **transposed** version of a matrix.
- Integrate into L06-T4: after printing the original matrix, call `transpose()` and print the transposed matrix.

**Sample Output:**
```

The original matrix:
|1	2	3	4|
|5	6	7	8|

Its transpose:
|1	5|
|2	6|
|3	7|
|4	8|

```

---

## Required Functions

Ensure the following functions are defined **with exact names and parameters**:

- `input_integers()` (provided)
- `create_matrix(rows, cols)`
- `print_matrix(matrix)`
- `transpose(matrix)`

---

## License

This repository is for **educational purposes only**.
```

---

Let me know if you’d like all `README.md` files bundled into one document or project archive.
