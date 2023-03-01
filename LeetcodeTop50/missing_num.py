def missingNum(nums):
    return sum(range(0, len(nums)+1)) - sum(nums)

print(missingNum([3, 0, 1]))

def missingNum2(nums):
    result = 0

    # XOR result with complete number sequence
    for number in range(len(nums) + 1):  # 0, 1, 2 ,3
        result ^= number

    # Essentially now result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3)

    # XOR result with values in nums
    for num in nums:  # 3,0,1
        result ^= num

    # result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3) ^ ( 3 ^ 0 ^ 1)

    # XOR of same values cancel each other out

    # result = (0) ^ (0 ^ 0)  ^ (1^1) ^ (2) ^ (3^3)
    # result =  0 ^ 0 ^ 0 ^ 2 ^ 0
    # result = 2

    return result  # 2

print(missingNum2([3, 0, 1]))