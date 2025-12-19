import math
def plusMinus(arr):
    positive = 0
    negative = 0
    null = 0
    for i in range(n):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            null += 1
    return "{:.6f} \n{:.6f} \n{:.6f}".format(positive / n , negative / n , null / n)


if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(plusMinus(arr))











