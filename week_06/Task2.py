def input_integers():
    line = input("Give integers separated by comma:\n")
    parts = line.split(",")
    return [int(p.strip()) for p in parts]

def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

nums = input_integers()
print("Original List:", nums)
unique = remove_duplicates(nums)
print("List with duplicates removed:", unique)
