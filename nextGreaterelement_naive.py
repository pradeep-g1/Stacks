def nextGreater(arr,size):
    for i in range(size):
        flag=True
        for j in range(i+1,size):
            if arr[j]>arr[i]:
                print(arr[j],end=" ")
                flag=True
                break
        else:
            print("-",end=" ")
    print()
arr=[30,50,20,15,25]
nextGreater(arr,len(arr))