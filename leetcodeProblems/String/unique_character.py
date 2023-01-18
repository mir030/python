from collections import Counter


def unique_character(s):
    s = list(s)
    result = [x for x in s if s.count(x) == 1]
    if len(result) > 0:
        return s.index(result[0])
    else:
        return -1


# Using dictionary and counters, better method
def unique_character_v2(s):
    dict = Counter(s)
    for i in s:
        if dict[i] == 1:
            return s.index(i)
    return -1


s = "aabb"
print(unique_character_v2(s))
