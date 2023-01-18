class Solution(object):
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            s = list(s)
            if s == s[::-1]:
                return True
            else:
                return False
        sub_str = ""
        result = ""
        count = 0
        for char in s:
            sub_str += char
            if isPalindrome(sub_str):
                if len(sub_str) > count:
                    result = sub_str
        return result


print(Solution.longestPalindrome("cbbd"))

