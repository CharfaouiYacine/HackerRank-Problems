if __name__ == '__main__':
    records = []
    low = float('inf')
    second_low = float('inf')
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        if score < low:
            second_low = low
            low = score

        elif (score > low) and (score < second_low):
            second_low = score
    names = []
    for i in records:
        if i[1] == second_low:
            names.append(i[0])

    names.sort()
    print(*names , sep='\n')