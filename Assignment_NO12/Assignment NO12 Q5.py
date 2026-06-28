def student_database():
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                roll = input("Roll Number: ")
                name = input("Name: ")
                age = int(input("Age: "))
                city = input("City: ")

                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

            except ValueError:
                print("Invalid Age!")

        elif choice == "2":
            roll = input("Enter Roll Number: ")
            print(students.get(roll, "Student Not Found"))

        elif choice == "3":
            for roll, details in students.items():
                print(roll, ":", details)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid Choice")


student_database()