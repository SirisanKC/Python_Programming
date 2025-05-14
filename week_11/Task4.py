import numpy as np


def matrix_input():
    rows = int(input("Enter amount of rows:\n"))
    cols = int(input("Enter number of columns:\n"))

    return rows, cols

def create_zero_matrix(rows, cols):
    zero_matrix = np.zeros((rows, cols), dtype=int)
    print("Zero-matrix of the given rows & columns is:")
    print("",zero_matrix)
    return zero_matrix

def modify_matrix(matrix):
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            matrix[row, col] = (row +1) * (col + 1)
    print("Matrix printed with np-formatting:")
    print(matrix)

def sort_matrix(matrix):
    sorted_matrix = np.sort(matrix, axis=None)
    print("\nMatrix sorted into one array:")
    print(sorted_matrix)
    return sorted_matrix

def print_matrix_with_semicolons(matrix):
    print("Matrix printed with elements separated by semicolons:")
    for row in matrix:
        print(";".join(map(str, row)) + ";")
    print()


def reshape_matrix(matrix):
    while True:
        try:
            print("Shaping the matrix. Please, enter the new dimensions.")
            new_rows = int(input("Enter amount of new rows:\n"))
            new_cols = int(input("Enter amount of new columns:\n"))
            reshaped_matrix = matrix.reshape(new_rows, new_cols)
            print("Newly shaped matrix is:")
            print("",reshaped_matrix)
            return reshaped_matrix
        except ValueError:
            print("Faulty shape. Please, try again.")


def matrix_statistics(matrix):
    max_value = np.max(matrix)
    min_value = np.min(matrix)
    total_sum = np.sum(matrix)
    
    print(f"Largest number in the matrix is: {max_value}")
    print(f"Smallest number in the matrix is: {min_value}")
    print(f"Sum of all values in the matrix is: {total_sum}")


def process_list():
    list_values = [int(item) for item in input("Enter the list items:\n").split()]
    unique_values = np.unique(list_values)
    print(f"Unique values are: {unique_values}")
def main():
    print("This program demonstrates use of numpy-matrix.")
    
    rows, cols = matrix_input()
  
    matrix = create_zero_matrix(rows, cols)

    modify_matrix(matrix)

    sorted_matrix = sort_matrix(matrix)

    print_matrix_with_semicolons(matrix)

    reshaped_matrix = reshape_matrix(matrix)

    matrix_statistics(reshaped_matrix)

    process_list()

main()