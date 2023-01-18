def moveZeros(nums):
    zeros = nums.count(0)
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0 and count < zeros:
            nums.remove(0)
            nums.append(0)
            count += 1
    return nums


nums = [0]
print(moveZeros(nums))