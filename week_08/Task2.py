import random
import string


def pass_gen(length):
    LETTERS = string.ascii_letters
    DIGITS = string.digits
    SPECIAL = string.punctuation
    COMB = LETTERS + DIGITS + SPECIAL

    password = ''.join(random.choice(COMB) for _ in range(length))
    return password

def main():
    random.seed(8292)

    while True:
        length = int(input("Enter the length of the password:\n"))
        if length <=0:
            print("Password length must be a positive integer.")
            continue
        generated_password = pass_gen(length)
        print(f"Generated password: {generated_password}")
        break

main()