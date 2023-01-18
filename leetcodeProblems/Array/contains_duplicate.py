# This one gives time limit exceeded on leetcode but valid solution
def contains_duplicate(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i] == array[j] and i != j:
                return True
    return False


# solution using set
def contains_duplicate_2(array):
    array_set = set(array)
    array_set_list = list(array_set)
    if len(array) != len(array_set_list):
        return True
    return False


nums = [2, 1, 3, 1]
output = contains_duplicate_2(nums)
print(output)
