class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapper = dict()
        string = ""
        for char in zip(s, t):
            if char[0] in mapper:
                if mapper[char[0]] != char[1]:
                    return False
            elif char[1] in string:
                return False
            else:
                mapper[char[0]] = char[1]
                string += char[1]
        return True
solution = Solution()
print(solution.isIsomorphic("badc", "baba"))