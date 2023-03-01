def titleToNumber(s):
    result = 0
    val = [i for i in range(1, 27)]
    key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    mapper = dict(zip(key, val))

    for i, char in enumerate(reversed(s)):
        result += mapper[char] * (26 ** i)
        print(mapper[char], result)
    return result

print(titleToNumber("FXSHRXW"))