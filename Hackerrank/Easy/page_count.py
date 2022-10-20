import math


def pageCount(n, p):
    # Write your code here
    t1 = math.ceil((p - 1) / 2)
    if n % 2 == 0:
        t2 = math.ceil((n - p) / 2)
    else:
        t2 = math.floor((n - p) / 2)

    return min(t1, t2)


n = 7
p = 5

print(pageCount(n, p))