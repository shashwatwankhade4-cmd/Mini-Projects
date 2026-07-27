x = 25
y = 30
z = 25

print("1. Is x greater than y?", x > y) 
      # Comparison operator > checks if x is greater than y, which is False since 25 is not greater than 30.

print("2. Is x equal to z?", x == z)
    
print("3. Is x <= y AND y != z?",
      (x <= y) and (y != z))
       #Comparison operator <= checks if x is less than or equal to y, which is True since 25 is less than 30.
       #Comparison operator != checks if y is not equal to z, which is True since 30 is not equal to 25.    
print("4. Is x > y OR x == z?",
      (x > y) or (x == z))
         #Comparison operator > checks if x is greater than y, which is False since 25 is not greater than 30.
         #Comparison operator == checks if x is equal to z, which is True since 25 is equal to 25.      