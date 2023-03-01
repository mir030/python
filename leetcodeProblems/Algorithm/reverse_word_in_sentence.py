class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        result = []
        for word in s_list:
            result.append(word[::-1])
        result = " ".join(result)
        return result

s = Solution()
print(s.reverseWords(s="Let's take LeetCode contest"))