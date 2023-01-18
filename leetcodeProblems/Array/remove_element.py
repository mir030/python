def remove_element(nums, val):
    if len(nums) == 0:
        return 0
    i = 0
    numbers = len(nums)
    for j in range(0, numbers):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = remove_element(nums, val)

print(k)
