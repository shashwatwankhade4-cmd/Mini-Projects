fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

print("First index of banana:", fruits.index('banana'))

print("First index of banana from index 2:",
      fruits.index('banana', 2))

try:
    print("Index of kiwi:", fruits.index('kiwi'))
except ValueError:
    print("Not found")