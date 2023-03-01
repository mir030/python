def longestSubstring(s):
    longest = ""
    for i in range(len(s)):
        current = ""
        left = i
        while left < len(s):
            if s[left] not in current:
                current = s[i:left+1]
                left += 1
            else:
                break
        longest = max(longest, current, key=len)
    return len(longest)

print(longestSubstring("bbbbb"))
