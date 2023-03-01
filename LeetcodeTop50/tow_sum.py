def twoSum(nums, target):
    for i in range(len(nums)-1):
        left = i + 1
        while left < len(nums):
            if nums[i] + nums[left] == target:
                return i, left
            else:
                left += 1

nums = [3, 3, 9, 1]
target = 6
print(twoSum(nums, target))