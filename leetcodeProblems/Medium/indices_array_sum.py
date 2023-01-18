def sum_of_elements(arr, sum):
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == sum:
                return i, j


arr = [1, 4, 10, 20, 3, 10]
print(sum_of_elements(arr, 33))
print(sum_of_elements(arr, 1))