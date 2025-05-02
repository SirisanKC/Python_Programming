# Python Basics - Week 3 Tasks

This repository contains a series of beginner-level Python exercises that focus on using conditional (selection) structures to make decisions, such as comparing values, controlling program flow, and performing logic-based operations.

## Getting Started

Use the **IDLE editor** for writing and running these programs. Each task should be saved in a separate file (e.g., `L03_T1.py`, `L03_T2.py`, etc.).

---

## Tasks Overview

### L03-T1: Integer Testing with Selection Structure
**Goal:** Determine if a given year is a leap year using conditional logic.

**Sample Output:**
```

Enter a year: 2023
2023 is not a leap year.

```

---

### L03-T2: Comparison of Character Strings with Several Conditions
**Goal:** Prompt user for program control, authenticate login, and handle errors.

**Key Features:**
- User input to stop or continue.
- Username and password check.
- Input validation and feedback.

**Sample Output:**
```

Do you want to stop the execution of the program (Y/N): N
Enter username: Pekka
Enter password: somerandomthing
User recognized!

```

---

### L03-T3: Implementation of a Simple Calculator Using Menu
**Goal:** Create a calculator supporting 4 operations (add, subtract, multiply, divide).

**Special Handling:**
- Division by zero.
- Invalid operation selection.
- Results formatted to two decimal places for division.

**Sample Output:**
```

Enter the first number: 36
Enter the second number: 0
...
Select the operation (1-4): 4
Error: Zero cannot be used as a divisor.

```

---

### L03-T4: Grade Calculation
**Goal:** Map a float value (score) to a grade using a fixed scale.

**Grading Scale:**
- 90–100 → 5  
- 80–89 → 4  
- 70–79 → 3  
- 60–69 → 2  
- 50–59 → 1  
- 0–49 → 0

**Sample Output:**
```

Enter your number of points: 56
Your grade is: 1

```

---

### L03-T5: String Comparison and Palindrome Testing  
**(Submit this task to CodeGrade on Moodle)**

**Goal:** 
1. Compare two strings for sorting or equality.
2. Check for the presence of the character `'z'`.
3. Determine if a third string is a **palindrome**.

**Sample Output:**
```

Enter word 1: jazz
Enter word 2: lazy
'jazz' comes earlier in order than 'lazy'.
Letter 'z' is found in word 'jazz'.
Letter 'z' is found in word 'lazy'.
Enter a word to be tested: python
'python' is not a palindrome.

```

---

## Notes

- Be precise with **spaces and formatting**—they affect grading in CodeGrade.
- Each **input** should end with `\n` for proper output alignment.
- Some tasks include hidden "Code Structure Tests"—you can safely ignore them unless stated otherwise.
