def powerOfThree(n):
    result = 0
    i = 0
    while result < n:
        result = 3 ** i
        i += 1
    if result == n:
        return True
    return False

print(powerOfThree(27))