students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add New Student")
    print("2. Update Marks")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            new_marks = float(input("Enter New Marks: "))
            students[roll]["marks"] = new_marks
            print("Marks Updated!")
        else:
            print("Student Not Found!")

    elif choice == "3":
        roll = input("Enter Roll Number: ")

        student = students.get(roll)

        if student:
            print(student)
        else:
            print("Student Not Found!")

    elif choice == "4":
        print("\nAll Students:")
        for roll, details in students.items():
            print("Roll No:", roll)
            print(details)

    elif choice == "5":
        roll = input("Enter Roll Number: ")

        removed = students.pop(roll, None)

        if removed:
            print("Student Removed!")
        else:
            print("Student Not Found!")

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")