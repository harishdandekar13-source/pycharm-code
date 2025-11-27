student = {}

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice=='1':
        sid=input("Enter Student ID: ")
        name=input("Enter Student Name: ")
        age=input("Enter Student Age: ")
        grade=input("Enter Student Grade: ")
        student[sid]={"name":name,"age":age,"grade":grade}
    elif choice=='2':
        info=student[sid]
        print("id",sid)
        print("name",name)
        print("age",age)
        print("grade",grade)



