def file_write(name):
    f = open(name, 'w')
    while True:
        user_input = input("Enter a name to save to the file (0 to stop):\n")
        if user_input == '0':
            break
        f.write(user_input + '\n')

    f.close()

def file_read(name):
    try:
        f = open(name, 'r')
        print(f"The following names are stored in the file '{name}':")
        for line in f:
            print(line.strip())

        f.close()

    except Error:
        print(f"Error: The file '{name}' does not exist.")


def main():
    filename = input("Enter the name of the file to be saved:\n")
    file_write(filename)
    file_read(filename)

main()