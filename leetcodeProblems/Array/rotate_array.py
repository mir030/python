# rotate 1 step at a time
def rotate_one_step(nums):
    i = 0
    for j in range(1, len(nums)):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
    return nums


# rotate all the k step at the same time
def rotate(array, no_of_rotation):
    if no_of_rotation > len(array):
        no_of_rotation = no_of_rotation - len(array)
    rotated_array = []
    for i in range((len(array) - no_of_rotation), len(array)):
        rotated_array.append(array[i])
    for i in range(0, len(array) - no_of_rotation):
        rotated_array.append(array[i])
    # the question asked for a no return and modify array in place
    for i in range(0, len(array)):
        array[i] = rotated_array[i]


nums = [1, 2, 3]
k = 2
rotate(nums, k)
print(nums)

