import time
import copy

def read_words(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


words = read_words("pseudo_words.txt")
words1 = copy.deepcopy(words)
words2 = copy.deepcopy(words)
words3 = copy.deepcopy(words)

start = time.time()
sorted_words = sorted(words1)
print(f"Time taken by sorted(): {time.time() - start:.6f} seconds")

start = time.time()
quicksorted_words = quicksort(words2)
print(f"Time taken by quicksort(): {time.time() - start:.6f} seconds")

start = time.time()
insertionSorted_words = insertionSort(words3)
print(f"Time taken by insertionSort(): {time.time() - start:.6f} seconds")
