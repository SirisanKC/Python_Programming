def file_handle(filename, mode, integers=None):
    try:
        if mode == 'read':
            file = open(filename, 'r')
            data = [int(line.strip()) for line in file]
            file.close()
            print(f"File '{filename}' read successfully, {len(data)} lines.")
            return data
        elif mode == 'write':
            file = open(filename, 'w')
            for integer in integers:
                file.write(f"{integer}\n")
            file.close()
            print(f"File '{filename}' was successfully written.")
    except (FileNotFoundError, ValueError, IOError):
        print(f"Error processing file '{filename}'.")
        return None

def main():
    input_file = input("Enter the name of the file to be read:\n")
    integers = file_handle(input_file, 'read')
    
    if integers is None:
        return

    output_file = input("Enter the name of the file to be written:\n")
    file_handle(output_file, 'write', integers)

main()