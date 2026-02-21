A = set(map(int, input().split())) # Reading the elements of A
n = int(input()) # Number of Sets N
verify = True
for i in range(n):
    N = set(map(int, input().split())) # reading the elements of N
    if A.issuperset(N) and len(A) > len(N):
        continue
    else:
        verify = False
        break

if verify:
    print(verify)
else:
    print(verify)
""" 
The whole point is to check if all elements of N are in A and the length of A is greater than the length of N.
if it's true then A is a strict super set of N , else A isn't and you can break immediately
"""