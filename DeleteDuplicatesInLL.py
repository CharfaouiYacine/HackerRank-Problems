def removeDuplicates(llist):
    current = llist
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next

        else:
            current = current.next
    return llist

"""The funny thing  is that i found this solution  by coincidence LoL"""