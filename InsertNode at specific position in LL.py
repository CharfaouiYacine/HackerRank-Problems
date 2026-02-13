def insertNodeAtPosition(llist, data, position):
    if llist is None: # if the list is empty
        new_node =SinglyLinkedListNode(data)
        llist = new_node
        return llist
    else:
        if position == 0: # if we want to add at position 0 aka head
            new_node =SinglyLinkedListNode(data)
            new_node.next = llist
            llist = new_node
            return llist
        else:
            count = 1
            current = llist
            while count < position:
                current =current.next
                count += 1
            new_node = SinglyLinkedListNode(data)
            new_node.next = current.next
            current.next = new_node
            return llist

"""Took me about 5 minutes , just separated the case if position is 0 
 from the other cases so it would be easier"""