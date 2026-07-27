# This program calculates area and perimeter of a rectangle.

length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Area helps determine the space inside the rectangle.
area = length * width

# Perimeter helps determine the total boundary length.
perimeter = 2 * (length + width)

"""
The results can be useful in real-life applications
such as flooring, fencing, and construction planning.
"""

# Displaying the calculated values clearly.
print("Area =", area)

# Showing perimeter separately for readability.
print("Perimeter =", perimeter)