def validParenthesis(s):
    if len(s) % 2 != 0:
        return False

    mapping = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if mapping[stack.pop()] != char:
                return False
    return True

print(validParenthesis("(("))

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapper={ 0:0, ")":"(", "}":"{", "]":"["}
        stack = []
        for i, char in enumerate(s):
            if char not in mapper:
                stack.append(char)
                print(stack)
            else:
                print("m " + mapper[char], "s " + s[i-1])
                if mapper[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return True

s = Solution()
print(s.isValid("{[]}"))
