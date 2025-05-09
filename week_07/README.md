# README: L07 Tasks - Python Program Documentation

## Overview

This project consists of multiple Python tasks that involve file handling, text processing, and a simple calculator program. The main goals are to practice reading and writing text and CSV files, performing file operations like copying, checking for palindromes, and implementing a calculator that uses file input and output.

## Tasks Overview

### L07-T1: Reading & Writing Text Files

**Description:**
This task involves writing two functions:

1. `file_write(name)`: Writes user-inputted names to a specified text file until the user enters "0".
2. `file_read(name)`: Reads the content of the file and prints each name stored.

**Example:**

```python
Enter the name of the file to be saved:
Exercise1.txt
Enter a name to save to the file (0 to stop):
John
Enter a name to save to the file (0 to stop):
Catherina
Enter a name to save to the file (0 to stop):
Anna
Enter a name to save to the file (0 to stop):
0

The following names are stored in the file 'Exercise1.txt':
John
Catherina
Anna
```

### L07-T2: Copying from One File to Another

**Description:**
The task involves copying the contents of one file to another using the `file_copy(fileA, fileB)` function. You specify the source file and destination file for the operation.

**Example:**

```python
Please give the name of the source file:
Exercise2.txt
Please give the name of the destination file:
out.txt
File copied successfully!
```

### L07-T3: Testing Data Inside a File (Palindromes)

**Description:**
This task reads a text file line by line and checks if each string is a palindrome. Palindromes are written to the output file `Palindromes.txt`.

**Example:**

```python
Enter the name of the file to be read:
Exercise3.txt
row 'BirdRib' is a palindrome.
row 'TacoBell' is not a palindrome.
...
```

The output file `Palindromes.txt` contains the palindromes found in the input file.

### L07-T4: CSV File Processing

**Description:**
This task reads a CSV file and prints only the second column values.

**Example:**

```python
Give the name of the CSV file:
Exercise4.csv
30
25
35
```

### L07-T5: Menu-Based Calculator Program (File Input/Output)

**Description:**
This is an extension of a previous calculator program where file handling is added. The program reads input values from a file, performs calculations (sum, subtraction, multiplication, division), and writes the results to an output file.

**Changes Made:**

1. The program reads numbers from a specified input file.
2. The program writes calculation results to an output file.
3. Handles edge cases like dividing by zero.

**Example:**

```python
Enter the name of the file to read:
Exercise5_numbers.txt
This calculator can perform the following functions:
1) Enter the values
2) Sum
3) Subtract
4) Multiply
5) Divide
0) Stop
Select the function (0-5):
1
Values 2 and 8 were read
This calculator can perform the following functions:
...
```

The output file `Exercise5_output.txt` will contain the results of the calculations.

---

## File Handling Instructions

* **File Opening and Closing**: Always use the method taught in the course for file handling. Files should be opened and closed correctly, and previous contents should be destroyed when writing to a file.
* **Spaces and Formatting**: Ensure that there are no extra spaces or formatting issues when displaying outputs, as this could cause errors in the grading process.

## File List

* `Exercise1.txt` – Input for names in **L07-T1**.
* `Exercise2.txt` – Source file for copying in **L07-T2**.
* `Exercise3.txt` – File containing strings to check for palindromes in **L07-T3**.
* `Exercise4.csv` – CSV file to extract the second column from in **L07-T4**.
* `Exercise5_numbers.txt` – Input numbers for the calculator in **L07-T5**.
* `Exercise5_output.txt` – Output file for the results of the calculator in **L07-T5**.

## How to Run the Program

1. Download the necessary files from Moodle.
2. Ensure Python is installed on your system.
3. Run the Python scripts corresponding to each task.
4. Follow the prompts in the terminal to provide file names and select menu options.


---

This README provides an overview and instructions for completing and running the tasks in this module.
