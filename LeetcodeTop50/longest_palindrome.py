def longestPalindrome(s):
    def palindrome(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    res = ""
    for i in range(len(s)):
        temp = palindrome(s, i, i+1)
        if len(temp) > len(res):
            res = temp

        temp = palindrome(s, i, i)
        if len(temp) > len(res):
            res = temp

    return res

print(longestPalindrome("cbbd"))