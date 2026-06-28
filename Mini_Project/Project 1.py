students = {}


# Function to calculate grade
def calculate_grade(percentage):

    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B+"
    elif percentage >= 50:
        return "B"
    else:
        return "F"


# Function to add student
def add_student():

    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("Roll Number already exists.")
            return

        name = input("Enter Student Name: ")

        marks = []

        for i in range(5):
            mark = float(input("Enter Marks of Subject " + str(i + 1) + ": "))
            marks.append(mark)

        total = 0

        for mark in marks:
            total += mark

        percentage = total / 5

        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        print("Student Added Successfully!")

    except ValueError:
        print("Invalid Input!")


# Function to view all students
def view_students():

    if len(students) == 0:
        print("No Student Records Found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for roll, data in students.items():

        print("Roll Number :", roll)
        print("Name        :", data["name"])
        print("Marks       :", data["marks"])
        print("Percentage  :", format(data["percentage"], ".2f"))
        print("Grade       :", data["grade"])
        print("-------------------------------------")


# Function to search student
def search_student():

    try:
        roll = int(input("Enter Roll Number to Search: "))

        if roll in students:

            data = students[roll]

            print("\nStudent Found")
            print("Roll Number :", roll)
            print("Name        :", data["name"])
            print("Marks       :", data["marks"])
            print("Percentage  :", format(data["percentage"], ".2f"))
            print("Grade       :", data["grade"])

        else:
            print("Student Not Found.")

    except ValueError:
        print("Invalid Roll Number.")
        # Function to update student
def update_student():

    try:
        roll = int(input("Enter Roll Number to Update: "))

        if roll not in students:
            print("Student Not Found.")
            return

        print("Enter New Details")

        name = input("Enter Student Name: ")

        marks = []

        for i in range(5):
            mark = float(input("Enter Marks of Subject " + str(i + 1) + ": "))
            marks.append(mark)

        total = 0

        for mark in marks:
            total += mark

        percentage = total / 5

        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        print("Student Updated Successfully!")

    except ValueError:
        print("Invalid Input.")


# Function to delete student
def delete_student():

    try:
        roll = int(input("Enter Roll Number to Delete: "))

        if roll in students:

            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":
                del students[roll]
                print("Student Deleted Successfully.")
            else:
                print("Deletion Cancelled.")

        else:
            print("Student Not Found.")

    except ValueError:
        print("Invalid Roll Number.")


# Function to display menu
def show_menu():

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    # Main Function
def main():

    while True:

        show_menu()

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank You for Using Student Management System")
            break

        else:
            print("Invalid Choice. Try Again.")


# Program Starts Here
if __name__ == "__main__":
    main()