from collections import Counter


def uniqueCharacter(s):
    for i, char in enumerate(s):
        if s.count(char) == 1:
            return i
    return -1

s = "leetcode"
s2 = "aabb"
print(uniqueCharacter(s))


def uniqueCharacter2(s):
    dct = Counter(s)
    for char in s:
        if dct[char] == 1:
            return s.index(char)
    return -1

print(uniqueCharacter2(s2))