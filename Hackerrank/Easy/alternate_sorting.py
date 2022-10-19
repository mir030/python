arr = [1, 1, 3, 2, 1]

def countingSort(arr):
    result = [0] * 100

    for a in arr:
        result[a] += 1

    return result