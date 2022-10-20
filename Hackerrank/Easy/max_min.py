arr = [1, 2, 3, 4, 6, 8, 10]
k = 2  # the number of elements to select from arr


# copied from hackerrank, better way of thinking
def maxMin(k, arr):
    # Write your code here
    arr.sort()
    unfair = 1000000000
    for i in range(len(arr)-k+1):
        d = arr[i+k-1] - arr[i]
        if d < unfair:
            unfair = d
    return unfair


# my code, takes too much time using the max, min
def maxMin2(k, arr):
    arr.sort()
    diff = []
    for i in range(0, len(arr)-k+1):
        new_arr = []
        for j in range(0, k):
            new_arr.append(arr[i+j])
        diff.append(max(new_arr) - min(new_arr))
    return min(diff)


print(maxMin(k, arr))