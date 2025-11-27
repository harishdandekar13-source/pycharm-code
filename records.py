# Dictionary to store student records
students = {}

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        sid = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grades = list(map(float, input("Enter grades separated by space: ").split()))
        students[sid] = {"Name": name, "Age": age, "Grades": grades}
        print("Student added successfully!")
        print("Current records:", students)

    elif choice == '2':
        if not students:
            print("No student records found.")
        for sid, info in students.items():
            print(f"\nID: {sid}, Name: {info['Name']}, Age: {info['Age']}, Grades: {info['Grades']}")

    elif choice == '3':
        sid = input("Enter student ID to search: ")
        if sid in students:
            info = students[sid]
            print(f"\nID: {sid}, Name: {info['Name']}, Age: {info['Age']}, Grades: {info['Grades']}")
        else:
            print("Student not found!")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")





