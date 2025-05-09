def file_copy(fileA, fileB):
    try:
        f_source = open(fileA, 'r')

        f_dest = open(fileB, 'w')

        try:
            

            for line in f_source:
                f_dest.write(line)

        finally:
            
            f_source.close()
            f_dest.close()

            print("File copied successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{fileA} does not found.")
    except IOError:
        print("Error: An error occured while copying the file.")

def main():
    source_file = input("Please give the name of the source file:\n")
    dest_file = input("Please give the name of the destination file:\n")
    file_copy(source_file, dest_file)


main()