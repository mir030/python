class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arrayToBST(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(mid)
    root.left = arrayToBST(nums[:mid])
    root.right = arrayToBST(nums[mid+1:])
    return root

    
