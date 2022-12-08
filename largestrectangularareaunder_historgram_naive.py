def maxarea(arr,size):
    res=0
    for i in range(size):
        count=1
        for j in range(i-1,-1,-1):
            if arr[j]>=arr[i]:
                count+=1
            else:
                break
        for j in range(i+1,size):
            if arr[j]>=arr[i]:
                count+=1
            else:
                break
        temp=count*arr[i]
        res=max(res,temp)
    return res
arr=[2,3,3,2]
print("max area is {} units".format(maxarea(arr,len(arr))))