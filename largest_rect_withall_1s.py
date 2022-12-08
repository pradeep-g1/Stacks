def largesthistrow(arr):
    res=0
    for i in range(len(arr)):
        count=1
        for j in range(i-1,-1,-1):
            if arr[j]>=arr[i]:
                count+=1
            else:
                break
        for j in range(i+1,len(arr)):
            if arr[j]>=arr[i]:
                count+=1
            else:
                break
        temp=count*arr[i]
        res=max(res,temp)
    return res
def max_rectange(arr):
    ans=[]
    result=largesthistrow(arr[0])
    for i in range(1,len(arr)):
        for j in range(len(arr)):
            if arr[i][j]:
                arr[i][j]+=arr[i-1][j]
        ans.append(max(result,largesthistrow(arr[i])))
    return max(ans)

arr = [[0, 1, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 0, 0]]

print("Maximum rectangle is: ", max_rectange(arr))