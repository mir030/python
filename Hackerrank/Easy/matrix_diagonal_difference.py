arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                sum1 += arr[i][j]
            if i + j == len(arr)-1:
                sum2 += arr[i][j]

    return abs(sum2-sum1)

diagonalDifference(arr)



