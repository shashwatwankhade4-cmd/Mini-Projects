import numpy as np

try:
    n = int(input("Enter how many random numbers to generate: "))

    if n <= 0:
        print("Please enter a positive number.")

    else:
        arr = np.random.randint(10, 101, n)

        print("\nGenerated Array:")
        print(arr)

        print("\nMean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))
        print("Minimum:", np.min(arr))
        print("Maximum:", np.max(arr))

        # Try reshaping into 2 rows
        if n % 2 == 0:
            matrix = arr.reshape(2, n//2)
            print("\nReshaped Matrix:")
            print(matrix)

            print("\nRow-wise Sum:")
            print(np.sum(matrix, axis=1))
        else:
            print("\nCannot reshape into a 2D matrix with equal rows.")

except ValueError:
    print("Invalid input! Please enter an integer.")
except Exception as e:
    print("Error:", e)