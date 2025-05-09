def is_palindrome(text):
    cleaned_text = text.strip().lower()
    return cleaned_text == cleaned_text[::-1]


def main():
    input_file_name = input("Enter the name of the file to be read:\n")
    output_file_name = 'Palindromes.txt'

    
    inputFile = open(input_file_name, 'r')
    outputFile = open(output_file_name, 'w')

    try:
        

        for row in inputFile:
            stripped_row = row.strip()

            if len(stripped_row) == 0:
                continue

            if is_palindrome(stripped_row):
                result = f"row '{stripped_row}' is a palindrome."
                print(result)

                outputFile.write(stripped_row + '\n')

            else:
                result = f"row '{stripped_row}' is not a palindrome."
                print(result)


    except FileNotFoundError:
        print(f"Error: The file '{input_file_name}' does not exist.")


    
    inputFile.close()
    outputFile.close()


main()