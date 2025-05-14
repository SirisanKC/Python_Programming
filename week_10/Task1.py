def employee_dictionary(dict_list):
    name = input("Enter worker's name:\n")
    workplace = input("Enter worker's workplace:\n")
    age = int(input("Enter worker's age:\n"))
    employee = {
        'Name': name,
        'Workplace': workplace,
        'Age': age

        }

    dict_list.append(employee)

def print_work_info(dict_list):
    print(f"List of Employees:")

    for employee in dict_list:
        print(f"Name: {employee['Name']}, Workplace: {employee['Workplace']}, Age: {employee['Age']}")
    
def main():
    dict_list = []

    num_employees = int(input("How many employees do you want to add?:\n"))

    for _ in range (num_employees):
        employee_dictionary(dict_list)

    print_work_info(dict_list)
   
    

main()