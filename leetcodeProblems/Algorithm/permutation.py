from collections import Counter
def permutations(s1, s2):
    d1 = Counter(s1)
    k = len(s1)
    for i in range(len(s2) - k + 1):
        sub = s2[i:i + k]
        d2 = Counter(sub)
        if d1 == d2:
            return True
    return False

print(permutations("ab", "adsafafsa"))