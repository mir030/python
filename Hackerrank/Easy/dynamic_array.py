def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    answers = []
    last_answer = 0
    for query in queries:
        type, x, y, = query
        idx = ((x ^ last_answer) % n)

        if type == 1:
            arr[idx].append(y)
        else:
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)

    return answers


n = 2
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

print(dynamicArray(n, queries))