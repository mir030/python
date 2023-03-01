class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

def inorderTraversal(root):
    def inorder(head):
        if head is None:
            return []
        else:
            return inorder(head.left) + [head.val] + inorder(head.right)
    return inorder(root)

print(inorderTraversal(root))
