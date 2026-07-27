

Manhwaname = "Lookism"
chapters = 500
price = 4999.99
available = True

# Printing values and data types
print( Manhwaname, type( Manhwaname))
print(chapters, type(chapters))
print(price, type(price))
print(available, type(available))

# Type conversion
float_number = float(chapters)
int_price = int(price)

print("Integer converted to float:", float_number)
print("Float converted to integer:", int_price)

# Explanation:
# float(500) becomes 500.0
# int(4999.99) removes the decimal part and becomes 4999
