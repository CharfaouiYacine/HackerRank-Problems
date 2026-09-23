def postOrder(root):
    if(root is None):
        return
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root,end=" ")
