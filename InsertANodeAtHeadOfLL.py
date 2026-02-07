class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def insertNodeAtHead(llist, data):
    if llist is None:
        llist = SinglyLinkedListNode(data)
        return llist
    else:
        new_node = SinglyLinkedListNode(data)
        new_node.next = llist
        llist = new_node
    return llist

"""
Yeah just like the one before it 
"""