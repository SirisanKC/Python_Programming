from datetime import datetime, timedelta

def identify():
    date_input= input("Enter the date and time in the format 'dd.mm.yyyy hh:mm':\n")
    try:
        dt = datetime.strptime(date_input, "%d.%m.%Y %H:%M")
        print(f"You gave year {dt.year}\nYou gave month {dt.month}\nYou gave day {dt.day}\nYou gave hour {dt.hour}\nYou gave minute {dt.minute}")

    except ValueError:
        print("Invalid date format. Please use 'dd.mm.yyyy hh:mm'.")


def age_days():
    birth_date = input("Enter your birthday as dd.mm.yyyy:\n")
    try:
        ad= datetime.strptime(birth_date, "%d.%m.%Y")
        ref_date = datetime(2024,1,1)
        age_days = (ref_date - ad).days
        print(f"On January 1, 2024, you were {age_days} days old.")

    except ValueError:
        print("Invalid date format. Please use 'dd.mm.yyyy'.")


def week_days():
    start_date = datetime(2024, 1, 1)
    for i in range(7):
        day = start_date + timedelta(days=i)
        print(day.strftime("%A"))



def months():
    for month in range(1, 13):
        month_name = datetime(2024, month, 1).strftime("%b")
        print(month_name)
       
              


        
def main():
    print("This program uses the datetime library to deal with time.")
    while True:
        choice = input("What do you want to do:\n1) Identify the components of a time object\n2) Calculate age in days\n3) Print the days of the week\n4) Print the months\n0) Stop\nYour choice:\n")
        
        if choice == '1':
            identify()
            print()

        elif choice == '2':
            age_days()
            print()

        elif choice == '3':
            week_days()
            print()

        elif choice == '4':
            months()
            print()

        elif choice == '0':
            print("See you again!")
            break
           

        else:
            print("Unknown choice, please try again.")
            print()

main()