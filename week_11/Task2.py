def find_pairs(num, target):
    pairs = []
    for i in range(len(num)):
        for j in range(i, len(num)):
            if num[i] + num [j] == target:
                
                pairs.append((num[i], num[j]))

    return pairs

def main():
    num = []

    while True:
        user_input = input("Enter an integer (or type 'done' to finish input):\n")

        if user_input == 'done':
            break

        try:
            nums = int(user_input)
            num.append(nums)

        except ValueError:
            print("Invalid input! Please enter an integer")

    try:
        target = int(input("Enter the target sum:\n"))

    except ValueError:
            print("Invalid input! Please enter an integer")
            return 


    pairs = find_pairs(num, target)

    if pairs:
        print(f"Pairs with a sum of {target}:")
        for pair in pairs:
            print(pair)

    else:
        print(f"No pairs found with a sum of {target}.")

main()