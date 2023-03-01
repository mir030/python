def squareRoot(x):
    if x == 1:
        return 1
    left, right = 0, x
    while left <= right:
        mid = (right + left)//2
        print(mid)
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            right = mid
        else:
            left = mid

print(squareRoot(100))


def squareRootv2(x):
    i = 0
    while i * i <= x:
        i += 1
    return i-1

print(squareRootv2(100))