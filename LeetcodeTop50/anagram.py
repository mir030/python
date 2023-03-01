def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    t = list(t)
    for char in s:
        if char not in t:
            return False
        else:
            t.remove(char)

    return True


s = "acca"
t = "cacc"
print(valid_anagram(s, t))