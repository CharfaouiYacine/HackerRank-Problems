arr1 = [2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,1]
arr = [2 ,4 ,6 ,8, 3]
#for i in range(len(arr)-1,0,-1):
   #if temp < arr[i-1]:
        #arr[i] = arr[i-1]
        #print(*arr)
    #if i == 0 and temp < arr[i]:
   #     arr[i]  = temp
  #      print(*arr)
 #   else:
#        arr[i] = temp
#        print(*arr)

temp = arr[len(arr) - 1]
i = len(arr)-1
while i>=0:
    if i ==0 and  temp < arr[i]:
        arr[i] = temp
        print(*arr)
        break
    elif temp <arr[i-1]:
        arr[i] = arr[i-1]
        print(*arr)
        i-=1
    else:
        arr[i] = temp
        print(*arr)
        break

