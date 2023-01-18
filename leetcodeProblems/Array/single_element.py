# This solution gets time limit exceeded
def single_element(array):
    for i in range(0, len(array)):
        count = 0
        for j in range(0, len(array)):
            if array[i] == array[j]:
                count += 1
        if count == 1:
            return array[i]


def single_element_2(array):
    array_set = set(array)
    array_set_list = list(array_set)
    for i in range(0, len(array_set_list)):
        if array_set_list[i] in array:
            array.remove(array_set_list[i])
    for i in range(0, len(array)):
        if array[i] in array_set_list:
            array_set_list.remove(array[i])
    return array_set_list[0]


def single_element_3(array):
    # Write your code here
    for num in array:
        if array.count(num) == 1:
            return num


nums = [4, 1, 2, 1, 2, 4, 5]
output = single_element_3(nums)
print(output)

