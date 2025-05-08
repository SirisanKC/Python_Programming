# Python Programming - Week 5 Tasks

This repository contains Python programming exercises centered around **functions**. The focus is on defining and using functions for logic, string operations, input/output, and building modular menu-based applications.

---

## Tasks Overview

### ✅ L05-T1: Three Simple Function Variations

This task includes:
- `print_lines()`: Prints a message, takes no input or return.
- `process_number(nr)`: Prints a number and its square.
- `print_whole_name()`: Asks for first and last names, returns the full name.

**Sample Output:**
```

Function 1:
This is printed in the function

Function 2:
Enter a number: 3
The input number is 3
The number squared is 9

Function 3:
Enter your first name: John
Enter your last name: Doe
The full name is John Doe

```

---

### ✅ L05-T2: Function with Parameters – Value Comparison

- Takes two integers and returns the larger.
- Asks for a third number to subtract from the larger, then compares again.
- Includes a tie message: `"The integers are the same."`

**Sample Output:**
```

Enter the first integer: 42
Enter the second integer: 39
42 is greater than 39
Enter the integer that is subtracted from the larger: 3
The integers are the same.

```

---

### ✅ L05-T3: String Containment Check Without `in`

- Function checks if one string is found inside another using **nested loops**.
- Returns True/False.
- Does not use the `in` keyword.

**Sample Output:**
```

Enter the first string: part
Enter the second string: apartment
The first string can be found in the second string.

```

---

### ✅ L05-T4: Compressed String 

- Compress a string using run-length encoding (e.g., `A13H3E2M`).
- Only add counts if greater than 1.
- Compute compression ratio and round to 2 decimal places.

**Requirements:**
- Function **must** receive and return a string.
- Code structure test is enforced.

**Sample Output:**
```

Give a string to compress: aaaabbbbbbbcdddddddddeekkkkkkk
Compressed string: a4b7cd9e2k7
Compressing ratio 0.37

```

---

### ✅ L05-T5: Modular Calculator 

Extend your previous calculator using modular functions:

#### Required Functions:
- `menu()`
- `enter_integer(text)`
- `sum(value1, value2)`
- `subtract(value1, value2)`
- `multiplication(value1, value2)`
- `division(value1, value2)`
- `main()`

**Features:**
- Menu-based calculator with loop.
- User can enter numbers once and perform multiple operations.
- Handles invalid choices and divide-by-zero.
- Returns string-formatted results from each function.

**Sample Output:**
```

Select the function (0-5): 5
Division 2 / 5 = 0.4

Select the function (0-5): 0
Bye.

```

---



## License

This repository is intended for **educational purposes only**.
```


Let me know if you’d like this README bundled with code templates or a zip-ready project layout.

