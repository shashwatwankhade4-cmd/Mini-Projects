marks = []

# Taking 5 subject marks
for i in range(5):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

print("Marks List:", marks)

# Add one more mark
extra_mark = float(input("Enter one more subject mark: "))
marks.append(extra_mark)

print("Updated Marks:", marks)

# Highest and Lowest
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

# Sort descending
marks.sort(reverse=True)
print("Marks in Descending Order:", marks)

# Average
average = sum(marks) / len(marks)
print("Average Marks:", average)

# Total subjects
print("Total Subjects:", len(marks))