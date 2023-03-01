class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for char in s:
            if char in t:
                t = t[t.index(char):]
                t = t[1:]
            else:
                return False
        return True

s = Solution()
print(s.isSubsequence("aaaaaa", "bbaaaa"))
