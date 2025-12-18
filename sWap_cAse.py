def swap_case(s):
    swap = ""
    for i in range(len(s)):
        if s[i].isupper():
            swap += s[i].lower()
        else:
            swap += s[i].upper()

    return swap


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)