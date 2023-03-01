def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    pivot = 0

    while pivot <= right:
        if sum(nums[left:pivot]) == sum(nums[pivot+1:]):
            return pivot
        else:
            pivot += 1

    return -1


print(pivotIndex([1, 2, 3]))
