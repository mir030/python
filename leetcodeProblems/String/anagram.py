def isAnagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_t == sorted_s:
        return True
    return False


s = "abc"
t = "caba"
print(isAnagram(s, t))

