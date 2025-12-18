def solve(s):
    cleaned = ""
    for i in range(len(s)):

        if i > 0 and s[i-1].isdigit():
            cleaned += s[i].lower()
        elif i == 0:
            cleaned += s[i].title()
        elif i > 0 and s[i-1].isspace():
            cleaned += s[i].title()
        else:
            cleaned += s[i]
    return cleaned

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)