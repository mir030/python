def majorityElement(nums):
    result = [x for x in nums if nums.count(x) > len(nums) // 2]
    return result[0]


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))

def majorityElement2(nums):
    major_element = nums[0]
    count = 0

    for num in nums:
        if major_element == num:
            count += 1
        elif count == 0:
            major_element = num
            count = 1
        else:
            count = -1
    return major_element

print(majorityElement2([1, 2, 1, 1, 2]))
