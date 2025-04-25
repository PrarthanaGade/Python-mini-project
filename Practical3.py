def _accept(row, mat, col):
    for i in range(row):
        for j in range(col):
            mat[i][j] = int(input(f"Enter the element at position ({i},{j}): "))


def _display(row, mat, col):
    for i in range(row):
        for j in range(col):
            print(mat[i][j], end=" ")
        print()  # Move to the next line after each row


def _addition(row, mat1, mat2, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result


def _subtraction(row, mat1, mat2, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j] = mat1[i][j] - mat2[i][j]
    return result


def _multiplication(row1, mat1, col1, row2, mat2, col2):
    if col1 != row2:
        print("Matrix multiplication not possible. Columns of the first matrix must equal rows of the second.")
        return None

    result = [[0 for _ in range(col2)] for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


def _transpose(row, mat, col):
    result = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j][i] = mat[i][j]
    return result


def _main():
    row1 = int(input("Enter the number of rows for the first matrix: "))
    col1 = int(input("Enter the number of columns for the first matrix: "))
    row2 = int(input("Enter the number of rows for the second matrix: "))
    col2 = int(input("Enter the number of columns for the second matrix: "))

    mat1 = [[0 for _ in range(col1)] for _ in range(row1)]
    mat2 = [[0 for _ in range(col2)] for _ in range(row2)]

    print("Enter the elements of the first matrix:")
    _accept(row1, mat1, col1)
    print("Enter the elements of the second matrix:")
    _accept(row2, mat2, col2)

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose (first matrix)")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            if row1 == row2 and col1 == col2:
                result = _addition(row1, mat1, mat2, col1)
                print("The sum of the two matrices is:")
                _display(row1, result, col1)
            else:
                print("Addition not possible. Matrices must have the same dimensions.")
        elif choice == 2:
            if row1 == row2 and col1 == col2:
                result = _subtraction(row1, mat1, mat2, col1)
                print("The difference of the two matrices is:")
                _display(row1, result, col1)
            else:
                print("Subtraction not possible. Matrices must have the same dimensions.")
        elif choice == 3:
            result = _multiplication(row1, mat1, col1, row2, mat2, col2)
            if result:
                print("The product of the two matrices is:")
                _display(row1, result, col2)
        elif choice == 4:
            result = _transpose(row1, mat1, col1)
            print("The transpose of the first matrix is:")
            _display(col1, result, row1)
        elif choice == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    _main()
