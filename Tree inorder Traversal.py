def inOrder(root):
    if(root is None):
        return
    else:
        inOrder(root.left)
        print(root,end=" ")
        inOrder(root.right)
