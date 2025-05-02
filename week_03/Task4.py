points = float(input("Enter your number of points:\n"))


if 90 <= points <= 100:
    grade = 5
elif 80 <= points < 90:
    grade = 4
elif 70 <= points < 80:
    grade = 3
elif 60 <= points < 70:
    grade = 2
elif 50 <= points < 60:
    grade = 1
elif 0 <= points < 50:
    grade = 0
else:
    grade = "Invalid input"  


print(f"Your grade is: {grade}")
