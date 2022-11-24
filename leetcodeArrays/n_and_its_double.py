class Solution(object):
    def checkIfExist(self, arr):
        for item in arr:
            if item*2 in arr:
                return "true"
        return "false"


arr = [3, 1, 7, 11]

solution = Solution()
print(solution.checkIfExist(arr))