import math
def diagonal_difference(arr):
    right_diagonal = 0
    left_diagonal = 0
    difference = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                left_diagonal += arr[i][j]

    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                right_diagonal += arr[i][j]


    difference = abs(left_diagonal - right_diagonal)

    return difference


if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonal_difference(arr)
    print(result)



