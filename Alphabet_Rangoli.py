my_alphabet = "abcdefghijklmnopqrstuvwxyz"
size = int(input("Enter the size: "))
rangoli = my_alphabet[:size]
max_width = size * 4 -3
prev_r,next_r,string,temp = "","","",""
d = []
for i in range(len(rangoli),0,-1):
    target = size
    while target >= size:
        if temp == "":
            temp = (prev_r + rangoli[i-1] + next_r).center(max_width,"-") + "\n"
        else:
            temp = (prev_r + "-" + rangoli[i-1] + "-" + next_r).center(max_width,"-") + "\n"

        d += [temp]
        string += temp
        if prev_r == "":
            prev_r = prev_r + rangoli[i-1]
        else:
            prev_r = prev_r + "-" + rangoli[i-1]
        if next_r == "":
            next_r = next_r + rangoli[i-1]
        else:
            next_r = rangoli[i-1]+ "-" +next_r
        target -= 1
d =d[:-1]
d.reverse()
fouad = "".join(d)
final = string + fouad
print(final)

