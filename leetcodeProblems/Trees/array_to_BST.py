# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root


input = [-10, -3, 0, 5, 9]
solution = Solution()

print(solution.sortedArrayToBST(input))