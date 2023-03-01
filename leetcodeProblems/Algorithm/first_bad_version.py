def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    def isBadVersion(mid):
        if mid == 1:
            return True
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        if isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        elif not isBadVersion(mid):
            l = mid + 1
        else:
            r = mid - 1

print(firstBadVersion(1))