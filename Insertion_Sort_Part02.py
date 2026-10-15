arr=[8 ,7, 6, 5, 4, 3 ,2 ,1]

for i in range(1,len(arr)):
    temp=arr[i]
    if i==1:
        if temp < arr[i-1]:
            arr[i] = arr[i - 1]
            arr[i-1] = temp
        print(*arr)
    else:
        j=i-1
        while j>=0 and i>=1:
            if arr[j]>temp:
                arr[i]=arr[j]
                arr[j]=temp
                i-=1
                j-=1
            else:
                i -= 1
                j -= 1
        print(*arr)









