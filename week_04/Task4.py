lower = int(input("Enter the lower limit of the range:\n"))
upper = int(input("Enter the upper limit of the range:\n"))
found = False

for i in range(lower, upper + 1):
    if i % 5 != 0:
        print(f"{i} is NOT divisible by 5, rejecting.")
        continue
    if i % 7 != 0:
        print(f"{i} is NOT divisible by 7, rejecting.")
        continue
    print(f"The number {i} is divisible by 5 and 7.")
    print("Stopping the search.")
    found = True
    break

if not found:
    print("No suitable value was found in the range.")
