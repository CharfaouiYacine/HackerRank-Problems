def compare_lists(llist1, llist2):
    equal = True
    while llist1 is not None and llist2 is not None:
        if llist1.data != llist2.data:
            equal = False
            return 0
        llist1 =llist1.next
        llist2 = llist2.next
        if llist1 is None and llist2 is not None or llist1 is not None and llist2 is None:
            return 0
    if equal is True:
        return 1

"""Maybe it can be more simplified but this was the best that i could do"""