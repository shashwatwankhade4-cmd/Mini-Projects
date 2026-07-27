# a) Tuple with 5 numbers
t1 = (10, 20, 30, 40, 50)

# b) Mixed tuple
t2 = (100, "Python", 99.5, True)

# c) Empty tuple (two ways)
t3 = ()
t4 = tuple()

# d) Single-element tuple
t5 = (99,)

# Note:
# A comma is required for a single-element tuple.
# (99) is treated as an integer, not a tuple.

print("t1 =", t1, type(t1))
print("t2 =", t2, type(t2))
print("t3 =", t3, type(t3))
print("t4 =", t4, type(t4))
print("t5 =", t5, type(t5))