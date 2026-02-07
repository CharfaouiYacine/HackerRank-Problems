def printLinkedList(head):
    if head is None:
        return
    else:
        while head is not None:
            print(head.data)
            head = head.next