def square_root(x):
    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2
        print(left, right, mid)
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1


print(square_root(10))