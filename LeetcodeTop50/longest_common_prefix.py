def longestCommonPrefix(strs):
    smallest_str = min(strs, key=len)
    prefix = ""
    for i, char in enumerate(smallest_str):
        left = 0
        while left < len(strs):
            if strs[left][i] != char:
                return prefix
            if left == len(strs) - 1:
                prefix += char
            left += 1
    return prefix


strs = ["flower", "flow", "flight"]
strs2 = ["cir", "car"]
print(longestCommonPrefix(strs))
print(longestCommonPrefix(strs2))
