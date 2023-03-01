def mergeSorted(nums1, nums2):

    for i in range(len(nums2)):
        nums1.remove(0)
        nums1.append(nums2[i])
    nums1.sort()

    return nums1


print(mergeSorted([1, 2, 3, 0, 0, 0], [2, 5, 6]))

"""Two pointer solution """
def merge(nums1, m, nums2, n):
    left = m - 1
    right = n - 1
    index = m + n - 1

    while left >= 0 and right >= 0:
        if nums1[left] > nums2[right]:
            nums1[index] = nums1[left]
            left -= 1
            index -= 1
        elif nums1[left] < nums2[right]:
            nums1[index] = nums2[right]
            right -= 1
            index -= 1
        else:
            nums1[index] = nums1[left]
            nums1[index-1] = nums2[right]
            left -= 1
            right -= 1
            index -= 2
    while right >= 0:
        nums1[index] = nums2[right]
        right -= 1
        index -= 1
    return nums1

nums1 = [1, 2, 0, 0, 0, 0]
nums2 = [1, 2, 3, 4]
print(merge(nums1, 2, nums2, 4))