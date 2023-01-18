def reverse_integer(x):
    abs_x = str(abs(x))
    list_x = list(abs_x)
    j = len(list_x) - 1
    for i in range(int(len(list_x)/2)):
        list_x[i], list_x[j] = list_x[j], list_x[i]
        j -= 1
    x_str = "".join(list_x)
    result = int(x_str)
    if x < 0:
        result = result * -1
    if result > pow(2, 31) - 1 or result < -pow(2, 31):
        return 0
    return result


x = -123
print(reverse_integer(x))

