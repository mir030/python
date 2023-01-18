def twoSum(nums, target):
        for i in range(len(nums)-1):
            left = i + 1
            while left < len(nums):
                if nums[i] + nums[left] == target:
                    return i, left
                else:
                    left += 1

arr = [2, 7, 11, 15]
target = 26
print(twoSum(arr, target))