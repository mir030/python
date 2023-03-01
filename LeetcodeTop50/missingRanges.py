def missingRanges(nums, lower, upper):
    nums = nums + [upper + 1]
    previous = lower
    output = []

    for num in nums:
        if num == previous + 2:
            output.append(f"{num-1}")
        elif num > previous + 2:
            output.append(f"{previous+1} -> {num-1}")
        previous = num
    return output


test_case1 = [0, 1, 3, 50, 75], 0, 99
test_case2 = [], -3, -1
print(missingRanges([0, 1, 3, 50, 75], 0, 99))