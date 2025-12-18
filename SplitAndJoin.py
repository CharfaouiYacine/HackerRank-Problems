def split_and_join(line):
    line1 = line.split(" ")
    line1 = "-".join(line1)
    return line1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)