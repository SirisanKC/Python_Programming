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

rows = int(input("Enter the number of rows:\n"))
cols = int(input("Enter the number of columns:\n"))

matrix = create_matrix(rows,cols)

print_matrix(matrix)