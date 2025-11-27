# Student Records Management System

students = {}  # Dictionary to store student records


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grades = list(map(int, input("Enter grades (space-separated): ").split()))

    students[student_id] = {
        "name": name,
        "age": age,
        "grades": grades
    }

    print("\nStudent added successfully!")
    print_student(student_id)


def display_all_students():
    if not students:
        print("\nNo student records available.")
        return

    print("\n--- All Student Records ---")
    for sid in students:
        print_student(sid)


def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        print("\nStudent Found:")
        print_student(student_id)
    else:
        print("\nStudent not found!")


def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("\nStudent deleted successfully!")
    else:
        print("\nNo student found with this ID.")


def update_grades():
    student_id = input("Enter Student ID to update grades: ")

    if student_id not in students:
        print("\nStudent not found!")
        return

    print("\nCurrent Grades:", students[student_id]["grades"])

    print("1. Add a new grade")
    print("2. Modify an existing grade")
    choice = int(input("Choose an option: "))

    if choice == 1:
        new_grade = int(input("Enter grade to add: "))
        students[student_id]["grades"].append(new_grade)
        print("\nGrade added successfully!")

    elif choice == 2:
        index = int(input("Enter index to modify (starting from 0): "))
        if 0 <= index < len(students[student_id]["grades"]):
            new_value = int(input("Enter new grade: "))
            students[student_id]["grades"][index] = new_value
            print("\nGrade updated successfully!")
        else:
            print("\nInvalid index!")

    else:
        print("\nInvalid option!")

    print_student(student_id)


def print_student(student_id):
    """ Helper function to print student details """
    student = students[student_id]
    print(f"ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print("--------------------------")


# ------------------------------- MAIN MENU -------------------------------

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Delete Student")
    print("5. Update Student Grades")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == '1':
        add_student()
    elif option == '2':
        display_all_students()
    elif option == '3':
        search_student()
    elif option == '4':
        delete_student()
    elif option == '5':
        update_grades()
    elif option == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
