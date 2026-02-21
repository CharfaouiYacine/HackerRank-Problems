T = int(input()) # The number of test cases

for i in range(T):
    count1 = int(input()) # number of elements in set A
    A = set(map(int,input().split())) # reading the elements of A
    count2 = int(input()) # number of elements in set B
    B = set(map(int,input().split())) # reading the elements of B
    if A.issubset(B): # checking if A is a subset of B
        print("True")
    else:
        print("False")
