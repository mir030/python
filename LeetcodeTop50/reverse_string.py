def reverseString(s):
    mid = len(s)//2
    j = len(s) - 1
    for i in range(mid):
        s[i], s[j] = s[j], s[i]
        j -= 1
    return s

s = ["H", "e", "l", "k", "o"]
print(reverseString(s))