def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other_word in strs:
            if other_word[i] != ch:
                return shortest[:i]
    return shortest


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix([""]))