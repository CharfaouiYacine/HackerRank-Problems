M = int(input())
M_set = set(map(int,input().split()))
N = int(input())
N_set = set(map(int,input().split()))
# You have to sort the set in order to print it  in ascending order
Difference = sorted(M_set.symmetric_difference(N_set))
for i in Difference:
    print(i)