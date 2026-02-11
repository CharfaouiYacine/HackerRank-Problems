"""
So yeah it took me a bit of time cause nothing was printing in the stdout (empty) but my code was correct
and the solution was to switch from  python3 to pypy3 and it worked
"""


def reversePrint(llist):
    arr = []
    while llist is not None:
        arr.append(llist)
        llist = llist.next
    arr.reverse()
    for i in arr:
        print(i.data)