def reverse(llist):
    arr = []
    while llist is not None:
        arr.append(llist.data)
        llist = llist.next
    arr.reverse()
    result = SinglyLinkedList()
    for i in arr:
        result.insert_node(i)
    return result.head

""" i wasn't able to solve it on my own cause i didn't pay attention on returning a node , 
i hope i don't make the same mistakes again
"""