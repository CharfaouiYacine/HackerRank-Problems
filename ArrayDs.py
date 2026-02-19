def reverseArray(a):
    i = 0
    j = len(a) -1
    count = len(a) / 2
    while i < count:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1
    return a

# or another stupid solution
def reverseArray(a):
    a.reverse()
    return a