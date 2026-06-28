square = lambda x: x * x

try:
    numbers = range(1, 21)

    squares = list(map(square, numbers))

    print("All Squares:")
    print(squares)

    print("Even Squares:")
    for i in squares:
        if i % 2 == 0:
            print(i)

except Exception as e:
    print("Error:", e)