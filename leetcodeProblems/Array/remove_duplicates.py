def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


nums = [1, 1, 2, 2, 3, 3, 3]
expectedNums = [1, 2, 3]

k = remove_duplicates(nums)

assert k == len(expectedNums)
for i in range(0, k):
    assert nums[i] == expectedNums[i]
