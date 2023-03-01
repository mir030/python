def moveZeroes(nums):
    counter = nums.count(0)
    nums[:] = [x for x in nums if x != 0]
    return nums + [0] * counter

print(moveZeroes([0, 1, 0, 3, 12]))