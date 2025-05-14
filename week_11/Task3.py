import numpy as np

def matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter {cols} values for row {i+1} (separated by space):\n").split()))
        matrix.append(row)
    return np.array(matrix)


def main():
    rows1 = int(input("Enter the number of rows for the first matrix:\n"))
    cols1 = int(input("Enter the number of columns for the first matrix:\n"))

    print(f"Enter values for a {rows1}x{cols1} matrix:")
    matrix1 = matrix_input(rows1, cols1)

    print("This is matrix 1:")
    print(matrix1)


    rows2 = int(input("Enter the number of rows for the second matrix:\n"))
    cols2 = int(input("Enter the number of columns for the second matrix:\n"))

    print(f"Enter values for a {rows2}x{cols2} matrix:")
    matrix2 = matrix_input(rows2, cols2)

    print("This is matrix 2:")
    print(matrix2)

    if matrix1.shape == matrix2.shape:
        print("Matrix sum:")
        print(matrix1 + matrix2)

    else:
        print("Error: sum not possible")

    if cols1 == rows2:
        print("Matrix multiplication:")
        print(np.dot(matrix1, matrix2))
    else:
        print("Error: multiplication not possible")

main()