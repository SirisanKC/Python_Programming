from datetime import datetime

def menu():
    input_date = input("Enter a date in YYYY-MM-DD format:\n")

    try:
        date = datetime.strptime(input_date, '%Y-%m-%d')
        print(f"{input_date} is a valid date.")

    except:
        print(f"{input_date} is not a valid date.")

menu()