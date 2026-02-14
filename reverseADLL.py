def reverse(llist):
    if llist is None:
        return None
    else:
        while llist.next is not None:
            llist = llist.next
        llist2 =DoublyLinkedList()
        while llist is not None:
            llist2.insert_node(llist.data)
            llist = llist.prev
        return llist2.head

"""This is my solution but there are other ones that are better cause they don't create another linked list 
Instead they just manipulate the nodes and the data in the same linked list"""