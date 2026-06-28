def manage_marks():
    marks = []

    while len(marks) < 5:
        try:
            mark = float(input(f"Enter mark {len(marks)+1}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid input! Enter numbers only.")

    print("\nMarks:", marks)
    print("Average:", sum(marks)/len(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

    marks.sort(reverse=True)
    print("Descending Order:", marks)


manage_marks()