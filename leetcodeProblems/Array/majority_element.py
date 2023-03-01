def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]

nums = [1, 2, 4, 3, 4, 4]
print(majorityElement(nums))


def majorityElement_moore(nums):
    majority_num = 0
    count = 0
    for num in nums:
        if count == 0:
            majority_num = num
        if majority_num != num:
            count -= 1
        else:
            count += 1
            print(majority_num)
    return majority_num

nums = [1, 2, 4, 3, 4, 5, 4, 4, 5]
print(majorityElement_moore(nums))