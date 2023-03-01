def moveZeroes(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(num)
    return nums

print(moveZeroes([0, 1, 0, 3, 12]))

def moveZeroes2(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

print(moveZeroes2([0, 1, 0, 3, 12]))