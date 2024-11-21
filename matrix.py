# Input the list of numbers from the user
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

# Input number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Check if the total number of elements matches the rows and columns
if len(numbers) != rows * columns:
    print("Error")
else:
    # Arrange the numbers into a matrix
    for i in range(rows):
        for j in range(columns):
            if j == columns - 1:  # Last column, no trailing comma
                print(numbers[i * columns + j], end="")
            else:
                print(numbers[i * columns + j], end=",")
        print()  # Move to the next line
