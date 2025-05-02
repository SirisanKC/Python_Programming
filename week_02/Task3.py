lword = input("Enter a long word:\n")

print(f"The first five letters are: {lword[:5]}")
print(f"The last five letters are: {lword[len(lword)-5::]}")
print(f"Letters 2, 3, 4, and 5 are: {lword[1:5]}")
print(f"Every second letter of the word: {lword[1::2]}")
print(f"The word backwards '{lword[::-1]}'")

sind = int(input("Enter start index:\n"))
eind = int(input("Enter end index:\n"))
step = int(input("Enter step\n"))

print(f"With these values '{lword}' produces this: {lword[sind:eind:step]}")

print(f"Your word is {len(lword)} characters long")