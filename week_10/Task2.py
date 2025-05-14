def remove_employee(employee_list):
    try:
        print("List of Employees:")
        for idx, employee in enumerate(employee_list, start=1):
            print(f"{idx}) Name: {employee['Name']}, Workplace: {employee['Workplace']}, Age: {employee['Age']}")
        
        employee_num = int(input("Enter the number of the employee to remove:\n"))
        
        if 1 <= employee_num <= len(employee_list):
            removed_employee = employee_list.pop(employee_num - 1)
            print(f"Removed employee: {removed_employee['Name']}")
        else:
            print("Invalid number. No employee removed.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

def modify_employee(employee_list):
    try:
        print("List of Employees:")
        for idx, employee in enumerate(employee_list, start=1):
            print(f"{idx}) Name: {employee['Name']}, Workplace: {employee['Workplace']}, Age: {employee['Age']}")
        
        employee_num = int(input("Enter the number of the employee to modify:\n"))
        
        if 1 <= employee_num <= len(employee_list):
            employee = employee_list[employee_num - 1]
            
            print("Enter the field to modify:")
            print("1) Workplace")
            print("2) Age")
            field_choice = int(input())
            
            if field_choice == 1:
                new_workplace = input("Enter new value for Workplace:\n").strip()
                new_workplace = new_workplace.replace('£', '')
                employee['Workplace'] = new_workplace
            elif field_choice == 2:
                new_age = int(input("Enter new value for Age:\n"))
                employee['Age'] = new_age
            else:
                print("Invalid choice. No changes made.")
        else:
            print("Invalid number. No employee modified.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

def print_employee(employee_list):
    print("List of Employees:")
    for employee in employee_list:
        print(f"Name: {employee['Name']}, Workplace: {employee['Workplace']}, Age: {employee['Age']}")

def main():
    employee_list = [
        {'Name': 'John', 'Workplace': 'LUT', 'Age': 25},
        {'Name': 'Jack', 'Workplace': 'Finnair', 'Age': 18},
        {'Name': 'Robin', 'Workplace': 'JBL', 'Age': 32},
        {'Name': 'Annie', 'Workplace': 'LUT', 'Age': 24},
        {'Name': 'Niels', 'Workplace': 'Microsoft', 'Age': 45}
    ]
    
    while True:
        print("Menu:")
        print("1) Remove an employee")
        print("2) Modify employee data")
        print("3) Print all employees")
        print("0) Exit")
        
        try:
            choice = int(input("Enter your choice:\n"))
            
            if choice == 1:
                remove_employee(employee_list)
            elif choice == 2:
                modify_employee(employee_list)
            elif choice == 3:
                print_employee(employee_list)
            elif choice == 0:
                print("See you again!")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()