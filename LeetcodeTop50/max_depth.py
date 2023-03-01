# I am using repeat to see how many iterations
repeat = 0
def maxDepth(root):
    global repeat
    repeat += 1
    if root is None:
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1

from tree_node import *

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

print(maxDepth(root))
print(repeat)