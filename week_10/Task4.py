import json

def load_students(filename):
    f = open(filename, 'r')
    student_list = json.load(f)
    f.close()
    return student_list

def print_students_by_age(student_list):
    ages = sorted(set(student['age'] for student in student_list if student['age'] >= 19))

    print("Select the ages of the students:")
    for i, age in enumerate(ages, 1):
        print(f"{i}) {age}")

    age_choice = int(input("Enter your selection:\n"))
    selected_age = ages[age_choice - 1]

    students_of_selected_age = [student for student in student_list if student['age'] == selected_age]
    
    for student in students_of_selected_age:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    
    print()

def print_students_by_course(student_list):
    predefined_courses = ["Computer Science", "History", "Math", "Art"]
    
    print("Select the course:")
    for i, course in enumerate(predefined_courses, 1):
        print(f"{i}) {course}")
    
    course_choice = int(input("Enter your selection:\n"))
    selected_course = predefined_courses[course_choice - 1]
    
    for student in student_list:
        if selected_course in student['courses']:
            print(f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['courses']}")
    
    print()


def print_students_name(student_list):
    print("Students whose name end with 'a':")
    for student in student_list:
        first_name = student['name'].split()[0]
        if first_name.endswith('a'):
            print(f"Student ID: {student['id']}, Name: {student['name']}")
 
    print()

def main():
    student_list = load_students('students.json')

    while True:
        print("What do you want to do?")
        print("1) Print students by age")
        print("2) Print students based on the course they are taking")
        print('3) Print students whose first names ends with the letter "a"')
        print("0) Stop the program")
      
        choice = int(input("Enter your choice:\n"))
        
        if choice == 1:
            print_students_by_age(student_list)
        elif choice == 2:
            print_students_by_course(student_list)
        elif choice == 3:
            print_students_name(student_list)
        elif choice == 0:
            print("See you again!")
            break
        else:
            print("Invalid choice. Please try again.\n")
           
if __name__ == "__main__":
    main()