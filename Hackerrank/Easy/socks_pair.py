arr = [1, 2, 1, 2, 1, 3, 2]


def sockMerchant(arr):
    counter = 0
    arr_set = set(arr)
    for a in arr_set:
        counter += arr.count(a) // 2
    return counter


sockMerchant(arr)