def mergerArray(nums1, m, nums2, n):
    length = (m + n)
    left = m - 1
    right = n - 1
    if m == 0:
        nums1[:] = nums2

    for i in range(length - 1, -1, -1):
        if nums2[right] >= nums1[left]:
            nums1[i] = nums2[right]
            right -= 1
        else:
            nums1[i] = nums1[left]
            left -= 1
        if left < 0 or right < 0:
            break
    while right >= 0:
        nums1[i-1] = nums2[right]
        right -= 1
        i -= 1
    return nums1

nums1 = [2, 2, 3, 4, 0, 0]
nums2 = [1, 1]
print(mergerArray(nums1, 4, nums2, 2))