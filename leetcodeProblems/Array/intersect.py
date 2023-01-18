def intersect(nums1, nums2):
    output = []
    for i in range(0, len(nums1)):
        for j in range(0, len(nums2)):
            if nums1[i] == nums2[j]:
                nums2.remove(nums2[j])
                output.append(nums1[i])
                break
    return output


nums2 = [1, 2]
nums1 = [1, 1, 3, 4, 5]
output = intersect(nums1, nums2)
print(output)