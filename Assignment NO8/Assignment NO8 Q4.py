fruits = {'apple', 'banana', 'mango'}

print("Original:", fruits)

# a) Add orange
fruits.add('orange')
print("After add orange:", fruits)

# b) Add banana again
fruits.add('banana')
print("After adding banana again:", fruits)

# c) Remove mango
fruits.remove('mango')
print("After removing mango:", fruits)

# d) Remove grape safely
fruits.discard('grape') #grape is not present in the set, so discard will not raise an error
print("After discard grape:", fruits)