def search(nums, target):
    # Find the pivot point
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l + r)//2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    # Perform binary search on left half
    l_start, l_end = 0, l-1
    while l_start <= l_end:
        mid = (l_end + l_start) // 2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            l_start = mid + 1
        else:
            l_end = mid - 1

    # Perform binary search on the right
    r_start, r_end = l, len(nums)-1
    while r_start <= r_end:
        mid = (r_start + r_end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            r_start = mid + 1
        else:
            r_end = mid - 1
    return -1

print(search([5, 6, 1, 2, 3, 4], 7))

