# Python Programming - Week 8 Tasks

This week's exercises focus on working with **standard Python libraries** like `math`, `random`, `fractions`, `datetime`, and using **exception handling** with `try-except`. Each task demonstrates practical applications of built-in modules.

---

## 📌 Tasks Overview

### ✅ L08-T1: Using Python Libraries — `math` & `random`
- Menu-based program with two main features:
  1. Calculate the area of a circle using `math.pi` and `pow()`.
  2. Random number guessing game using `random.randint` and `random.seed(1)`.
- Input validation and looped guessing until success.
- Unrecognized menu options prompt: `"Unknown choice, please try again."`

**Sample Output:**
```

With a radius of 7, the area of the circle is 153.94.
Correct! You used 7 tries to guess the correct integer.

```

---

### ✅ L08-T2: Random Password Generator
- Use `random.seed(8292)` for reproducibility.
- Use `string.ascii_letters`, `string.digits`, `string.punctuation` to build character pool.
- Generate a password of user-specified length using `random.choice()`.

**Sample Output:**
```

Enter the length of the password: 16
Generated password: bQ:\<AXWQ7\`SZ@*i*

```

---

### ✅ L08-T3: Fractions with `fractions` Module
- Ask user for numerators and denominators of two fractions.
- Ask for an exponent.
- Perform and display:
  - Addition, Subtraction, Multiplication, Division, Exponentiation

**Sample Output:**
```

Sum: 26/37 + 17/41 = 1695/1517
Power: (26/37)\*\*3 = 17576/50653

```

---

### ✅ L08-T4: Working with `datetime`
- Menu-driven interface using `datetime` and `timedelta`.
- Four options:
  1. Extract date/time components from a string input.
  2. Calculate age in days as of 01.01.2024.
  3. Print names of weekdays using `strftime`.
  4. Print month abbreviations.

**Sample Output:**
```

You gave year 2024
On January 1, 2024, you were 8451 days old.
Jan Feb Mar ... Dec

```

---

### ✅ L08-T5: Date Validation with `try-except`
- Ask for a date in `YYYY-MM-DD` format.
- Use `try-except` with `datetime` to determine if it is valid.

**Sample Output:**
```

Enter a date in YYYY-MM-DD format:
2023-09-31
2023-09-31 is not a valid date.

```



## 📚 Libraries Used

- `math`
- `random`
- `string`
- `fractions`
- `datetime`

---

## License

This repository is for **educational purposes only**.
```

---

Let me know if you'd like this combined with the previous README files into a single document.
