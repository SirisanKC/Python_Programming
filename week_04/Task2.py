vowels = "aeiouAEIOU"
string = input("Enter a string:\n")
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels is: {count}")
