def diagonalDifference(arr):
    n = len(arr)
    leftDiagonal = 0
    rightDiagonal = 0

    for i in range(n):
        leftDiagonal += arr[i][i]
        rightDiagonal += arr[i][n - 1 - i]
    return abs(rightDiagonal - leftDiagonal)


m = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
print(diagonalDifference(m))
