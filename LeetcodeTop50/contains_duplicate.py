def containsDuplicate(nums):
    result = [True for x in nums if nums.count(x) > 1]
    if True in result:
        return True
    return False

def containsDuplicate2(nums):
    nums_set = set()
    for num in nums:
        if num not in nums_set:
            nums_set.add(num)
        else:
            return True
    return False

print(containsDuplicate2([1, 2, 3, 1]))

