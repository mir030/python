def missingElement(nums):
    n = len(nums)
    return n*(n+1)//2 - sum(nums)

nums = [0, 1, 3]
print(missingElement(nums))