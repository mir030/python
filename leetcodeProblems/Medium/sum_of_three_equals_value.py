def sum_of_three_equals_value(nums, value):
    nums.sort()
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            if nums[i] + nums[left] + nums[right] == value:
                return True
            elif nums[i] + nums[left] + nums[right] < value:
                left += 1
            else:
                right -= 1
    return False


nums = [1, 2, 5, 7, 3, 4]
value = 6

print(sum_of_three_equals_value(nums, value))