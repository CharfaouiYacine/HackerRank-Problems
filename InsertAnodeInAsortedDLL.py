def sortedInsert(llist, data):
    if llist is None:    #In case the linked list is empty
        new_node = DoublyLinkedListNode(data)
        llist = new_node
        return llist
    elif llist.next is None: # In case the Linked list has one element
        if llist.data <= data: # add at the beginning
            new_node = DoublyLinkedListNode(data)
            llist.next = new_node
            new_node.prev = llist
            return llist
        else: # add after the head
            new_node = DoublyLinkedListNode(data)
            new_node.next = llist
            llist.prev = new_node
            return new_node

    else: # Case of linked list having more the one element
        current = llist
        if current.data >= data: # means that we will add at the beginning
            new_node = DoublyLinkedListNode(data)
            new_node.next = current
            current.prev = new_node
            llist = new_node
            return llist

        else:
            while (current.next is not None and current.next.data <= data):
                current = current.next
            if current.next is None: # means that we reached the tail
                new_node = DoublyLinkedListNode(data)
                current.next = new_node
                new_node.prev = current
                return llist
            else: # means we are in the middle
                new_node = DoublyLinkedListNode(data)
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                new_node.next.prev = new_node
                return llist

""" There are another simpler codes but they don't cover each case , 
this code cover all cases and will work in any scenario  
"""
