import math
import random

def circle_area():
    radius = int(input("Enter the radius of the circle as an integer:\n"))
    area = round(math.pi* math.pow(radius,2), 2)
    print(f"With a radius of {radius}, the area of the circle is {area}.")

def random_number():
    random.seed(1)
    number_to_guess = random.randint(0,1000)
    tries = 0
    print("Guess the integer drawn by the program.")

    while True:
        guess = int(input("Enter an integer between 0 and 1000:\n"))
        tries += 1
        if guess < number_to_guess:
            print("The requested number is higher.")

        elif guess > number_to_guess:
            print("The requested number is lower.")

        else:
            print(f"Correct! You used {tries} tries to guess the correct integer.")
            break
            
    


def main():
    print("This program uses libraries to solve tasks.")

    while True:
        choice = input("What do you want to do:\n1) Calculate the area of the circle\n2) Guess the number\n0) Stop\nYour choice:\n")
        if choice == '1':
            circle_area()
            print()

        elif choice == '2':
            random_number()
            print()

        elif choice == '0':
            print("See you again!")
            break

        else:
             print("Unknown choice, please try again.")
             print()

main()