def symmetricTree(root):
    def symmetry(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val != r.val:
            return False

        outer_sym = symmetry(l.left, r.right)
        inner_sym = symmetry(l.right, r.left)
        return outer_sym and inner_sym
    return symmetry(root, root)


