def pascalsTriangle(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    if numRows = 5
           [
                 [1],
                [1,1],
               [1,2,1],
              [1,3,3,1],
             [1,4,6,4,1]
           ]
    """
    result = [[1], [1, 1]]
    row = []
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return result
    for i in range(3, numRows + 1):
        for j in range(i-2):
            row.append(sum(result[-1][j:j+2]))
        result.append(list([1] + row + [1]))
        row = []
    return result


print(pascalsTriangle(1))

