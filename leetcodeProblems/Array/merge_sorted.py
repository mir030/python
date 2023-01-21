def mergeSorted(nums1, nums2):

    for i in range(len(nums2)):
        nums1.remove("0")
        nums1.append(nums2[i])
    nums1.sort()

    return nums1


print(mergeSorted([1, 2, 3], [2, 5, 6]))