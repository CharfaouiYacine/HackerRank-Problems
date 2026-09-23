def preOrder(root):
    current = root
    if(current is None):
        return
    else:
        print(current.info,end=" ")
        preOrder(current.left)
        preOrder(current.right)