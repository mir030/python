def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    arr_min = arr[0: 4]
    arr_max = arr[1: 5]
    print(sum(arr_min), sum(arr_max))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
