# Python Programming - Week 10 Tasks

This week focuses on working with **dictionaries**, **CSV & JSON data processing**, and **creating your own modules and classes**. You'll manipulate employee records, parse Titanic passenger and student data, and build a basic class with methods.

---

## 📌 Tasks Overview

### ✅ L10-T1: Employee Dictionary
- Implement:
  - `employee_dictionary(dict_list)` — prompts for name, workplace, and age, then appends a dictionary to the list.
  - `print_work_info(dict_list)` — prints all employee info in a readable format.
- The main program:
  - Asks how many employees to add.
  - Calls both functions accordingly.

**Sample Output:**
```

List of Employees:
Name: John, Workplace: LUT, Age: 40
...

```

---

### ✅ L10-T2: Employee Dictionary 2
- Use a pre-defined list of employees.
- Implement a **menu-based** program with:
  1. `remove_employee(employee_list)`
  2. `modify_employee(employee_list)`
  3. `print_employee(employee_list)`
- Add error handling for invalid inputs.
- Modify either the workplace or age of selected employee.

**Sample Menu:**
```

Menu:

1. Remove an employee
2. Modify employee data
3. Print all employees
4. Exit

```

---

### ✅ L10-T3: Titanic Passenger Data Processing
- Use the `titanic.csv` file (already in CodeGrade).
- Calculate:
  - Number of male passengers.
  - Number of female passengers.
  - Average age (rounded to closest integer).
  - Age of the oldest passenger.
- Ignore passengers with missing age data.

**Sample Output:**
```

The number of male passengers: 5
The average age of passengers: 28

```

---

### ✅ L10-T4: JSON File Handling
- Use `students.json` (already in CodeGrade).
- Create and use these functions:
  1. `print_students_by_age(student_list)`
  2. `print_students_by_course(student_list)`
  3. `print_students_name(student_list)`
- Each function prompts for a filter (e.g., age, course) and prints matching students.
- Filter names ending in the letter `"a"`.

**Sample Output:**
```

Students whose name ends with 'a':
Student ID: 6, Name: Sophia Anderson
...

```

---

### ✅ L10-T5: Creating Your Own Module
- Create a file `person.py` containing:
  - `__init__(self, name, age)`
  - `introduce(self)`
  - `celebrate_birthday(self)`
- Create a program `L10-T5.py` that:
  - Imports `person`
  - Creates two people: Valtteri (35) and Kimi (45)
  - Calls methods to:
    - Introduce both
    - Celebrate Kimi’s birthday
    - Introduce Kimi again

**Sample Output:**
```

My name is Valtteri, and I am 35 years old.
My name is Kimi, and I am 45 years old.
My name is Kimi, and I am 46 years old.

```



## 📚 Topics Covered

- Dictionaries & Lists
- File I/O (CSV and JSON)
- Class & Method Definitions
- Menu-based User Interaction
- Exception Handling

---

## 📄 License

This repository is for **educational use only** as part of the Python Programming course.
```

---

Let me know if you’d like all 10 weekly `README.md` files compiled into one or organized into a GitHub-style structure.

