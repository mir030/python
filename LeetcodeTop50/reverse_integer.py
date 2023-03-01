def reverseInteger(x):
    result = str(abs(x))[::-1]
    result = int(result)
    if x < 0:
        result = result * -1

    if -2 ** 31 < result < 2 ** 31 - 1:
        return result
    else:
        return 0

print(reverseInteger(-120))