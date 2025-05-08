def contains(a, b):
    for i in range(len(b) - len(a) + 1):
        match = True
        for j in range(len(a)):
            if b[i + j] != a[j]:
                match = False
                break
        if match:
            return True
    return False

s1 = input("Enter the first string:\n")
s2 = input("Enter the second string:\n")

if contains(s1, s2):
    print("The first string can be found in the second string.")
else:
    print("The first string cannot be found in the second string.")
