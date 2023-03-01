def pascalTriangle(num_rows):
    result = [[1], [1, 1]]

    if num_rows == 1:
        return [[1]]
    elif num_rows == 2:
        return result

    for i in range(2, num_rows):
        row_sum = []
        for j in range(i-1):
            row_sum.append(result[i-1][j] + result[i-1][j+1])
        row_sum = [1] + row_sum + [1]
        result.append(row_sum)
    return result

print(pascalTriangle(5))