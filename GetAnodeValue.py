def getNode(llist, positionFromTail):
    current = llist
    count = 1
    while current.next is not None:
        current = current.next
        count +=1
    desired_position = count - positionFromTail
    count = 1
    while  count != desired_position and llist.next is not None:
        llist = llist.next
        count += 1
    return llist.data

"""This solution takes O(n) but there is a faster solution  using only one while loop
explanation: let  the head start moving   and use a count that increase with it ,when the counter reaches the same
value as the positionFrom tail we create a new var called current = llist , and they both start moving until llist
reaches the very end  , we will find that current will be exactly at the desired position we want
"""
