import numpy as np

# Generate marks for 10 students and 5 subjects
marks = np.random.randint(30,101,(10,5))

print("Student Marks:")
print(marks)

# Total marks of each student
total = marks.sum(axis=1)

# Average marks
average = marks.mean(axis=1)

print("\nTotal Marks:")
print(total)

print("\nAverage Marks:")
print(average)

# Highest scorer
highest = total.argmax()

# Lowest scorer
lowest = total.argmin()

print("\nHighest Scorer: Student", highest + 1)
print("Marks:", marks[highest])

print("\nLowest Scorer: Student", lowest + 1)
print("Marks:", marks[lowest])

# Overall class statistics
print("\nClass Mean:", marks.mean())
print("Class Standard Deviation:", marks.std())

# Top 3 students
top3 = np.argsort(total)[-3:]

print("\nTop 3 Students:")
print(top3 + 1)

print("\nMarks of Top 3 Students:")
print(marks[top3])

# Reshape demonstration
reshaped = marks.reshape(5,10)

print("\nReshaped Array (5x10):")
print(reshaped)