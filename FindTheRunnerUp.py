if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

A = list(arr)

max1 = float('-inf')
max2 = float('-inf')
for i in A:
    if i > max1:
        max2 = max1
        max1 = i
    if (i < max1) and (i > max2):
        max2 = i
print(max2)

