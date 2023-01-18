def reverse_string(s):
    j = len(s)-1
    for i in range(int(len(s)/2)):
        s[i], s[j] = s[j], s[i]
        j -= 1

    return s


s = ["h", "e", "l", "l", "o"]
print(reverse_string(s))