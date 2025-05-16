def sum_of_list_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_of_list_recursive(numbers[1:])


nums = [3, 5, 7, 10]
print(f"Sum of {nums} is {sum_of_list_recursive(nums)}")
