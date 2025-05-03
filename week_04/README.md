# Python Programming - Week 4 Tasks

This repository contains tasks focused on **repetition structures** (loops) in Python. These tasks aim to strengthen your understanding of different looping mechanisms, string manipulation, condition-based iteration, and enhancing previous code with structured menus.

---

## Tasks Overview

### ✅ L04-T1: Different Repetition Structures
**Goal:** Use both `for` and `while` loops to print all integers from a start to an end value (inclusive).

**Sample Output:**
```

Enter the starting value:
1
Enter the ending value:
10
Implementation with a for loop:
1 2 3 4 5 6 7 8 9 10
Implementation with a while loop:
1 2 3 4 5 6 7 8 9 10

```

---

### ✅ L04-T2: Repetition Structure with String
**Goal:** Count the number of vowels (case-insensitive) in a given string.

**Sample Output:**
```

Enter a string:
The USA, the shorthand for the United States of America.
Number of vowels is: 18

```

---

### ✅ L04-T3: Loop with Multiple Termination Conditions
**Goal:** Print values of `a` (doubling) and `b` (increasing by 100) until either exceeds 1000.

**Sample Output:**
```

Enter a:
5
Enter b:
333
a: 5 b: 333
a: 10 b: 433
...
b exceeded 1000

```

Handles scenarios where:
- a exceeds 1000  
- b exceeds 1000  
- both exceed 1000

---

### ✅ L04-T4: Extensions of Repeat Structures *(Submit to CodeGrade)*
**Goal:** Use `for`, `break`, and `continue` to find the first number divisible by both 5 and 7 within a user-defined range. 

- Must include **all three**: `for-loop`, `break`, and `continue`.

**Sample Output:**
```

Enter the lower limit of the range:
99
Enter the upper limit of the range:
113
...
The number 105 is divisible by 5 and 7.
Stopping the search.

```

Handles case where **no result is found**:
```

No suitable value was found in the range.

```

---

### ✅ L04-T5: Menu-based Calculator *(Submit to CodeGrade)*
**Goal:** Extend the calculator from **L03-T3** with a loop-based menu. The calculator should:

- Let user enter numbers once.
- Perform operations: sum, subtract, multiply, divide, power.
- Allow repeated calculations until stopped.
- Validate for zero division.
- Handle invalid menu selections.

**Sample Output:**
```

This calculator can perform the following functions:

1. Enter numbers
2. Sum
3. Subtract
   ...
4. Stop
   Select function (0-6):
   7
   Unknown selection, try again.
   ...
   Select function (0-6):
   0
   Stopping
   Bye

```

## License

This repository is intended for **educational purposes only**.

