def prevgreater(arr,size):
    for i in range(size):
        flag=False
        for j in range(i-1,0,-1):
            if arr[j]>arr[i]:
                print(arr[j],end=" ")
                flag=True
                break
        if not flag:
            print("-",end=" ")
    print()
arr=[30,50,20,15,25]
prevgreater(arr,len(arr))

#time complexity is :- O(n^2)

