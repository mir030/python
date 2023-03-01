def single_element(nums):
    result = [x for x in nums if nums.count(x) == 1]
    return result[0]


def single_element2(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result ^= nums[i]
    return result


print(single_element2([4, 1, 2, 1, 2]))