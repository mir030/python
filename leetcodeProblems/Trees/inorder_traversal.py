def inorderTraversal(root):
    def inorder(head):
        if head is None:
            return []
        else:
            return inorder(head.left) + [head.val] + \
                   inorder(head.right)

        return inorder(root)
