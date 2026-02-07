"""
Yeah so this is my solution  and it's really stupid , i solved it now at night and i am pushing it at the same
time , so it's really stupid i know but it does the job ( work for everycase in Hackerrank)
"""


def deleteNode(llist, position):
    count = 0
    current = llist
    if position == 1:
        llist.next = llist.next.next
        return llist
    else:
        while count < position - 1:
            count += 1
            current = current.next

        if count == 0:
            llist = llist.next
            return llist

        else:
            current.next = current.next.next
            return llist