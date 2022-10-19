import itertools

a = [2, 1, 3]
b = [7, 8, 9]
k = 10


def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        if a + b < k:
            return 'NO'

    return 'YES'

twoArrays(k, a, b)

