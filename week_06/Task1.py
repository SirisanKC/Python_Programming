def input_integers():
    line = input("Give integers separated by comma:\n")
    parts = line.split(",")
    return [int(p.strip()) for p in parts]

def reverse_list(numbers):
    reversed_list = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])
    return reversed_list

nums = input_integers()
rev = reverse_list(nums)
print("Reversed list:", rev)
