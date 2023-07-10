import sys


def flippingMatrix(matrix):
    n = len(matrix) / 2
    v = 0
    t = 0
    row = 0
    col = 0

    while row < n:
        while col < n:
            v = -sys.maxsize - 1
            v = max([matrix[row][col], v])
            v = max([matrix[row][2 * n - col - 1], v])
            v = max([matrix[2*n - row - 1][col], v])
            v = max([matrix[2 * n - row - 1][2 * n - col - 1], v])

            t += v
            col += 1
        row += 1

    return t


m = [[1, 2], [3, 4]]

print(flippingMatrix(m))
