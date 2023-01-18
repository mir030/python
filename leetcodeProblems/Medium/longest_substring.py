def lengthOfLongestSubstring(s: str) -> int:
    # Base Case
    if len(s) == 1:
        return 1

    count, s_result = 0, ''

    for char in s:
        if char not in s_result:
            s_result += char
            print("if > " + s_result)
        else:
            print(s_result.index(char))
            s_result = s_result[s_result.index(char) + 1:] + char
            print("else > " + s_result)

        if len(s_result) > count:
            count = len(s_result)

    return count

s= "abacda"
print(lengthOfLongestSubstring(s))

