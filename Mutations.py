def mutate_string(string, position, character):
    change = list(string)
    change[position]= character
    result  = "".join(change)
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)