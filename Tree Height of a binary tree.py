def height(root):
    heighleft = 0
    heighright = 0
    if root is None or (root.left is None and root.right is None):
        return 0
    else:
        if root.left is not None:
            heighleft = height(root.left)
        if root.right is not None:
            heighright = height(root.right)
        if heighleft > heighright:
            return heighleft + 1
        else:
            return heighright + 1



