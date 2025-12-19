def staircase(n):
    result = ""
    for i in range(1, n+1):
        result +=("#"*i).rjust(n) + "\n"
    print(result)
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
