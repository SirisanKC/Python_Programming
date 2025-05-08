def create_matrix(rows, cols):
    matrix =[]

    for i in range(rows):
        while True:
            user_input = input(f"Give row {i + 1}:\n")
            elements = user_input.split()

            if len(elements) == cols:
                matrix.append([int(e) for e in elements])
                break

            else:
                print("Error: Invalid number of elements in the row. Please try again.")


    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("|" + "\t".join(map(str, row)) + "|")

def transpose(matrix):
    transposed = [[0]* len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed


rows = int(input("Enter the number of rows:\n"))
cols = int(input("Enter the number of columns:\n"))

matrix = create_matrix(rows,cols)

print("The original matrix:")
print_matrix(matrix)

transposed_matrix = transpose(matrix)

print("Its transpose:")
print_matrix(transposed_matrix)