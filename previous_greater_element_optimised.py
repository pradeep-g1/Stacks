from collections import deque
def prevgreater(arr,size):
    stack=deque()
    stack.append(arr[0])
    print("-",end=" ")
    for i in range(1,size):
        while len(stack)>0 and stack[-1]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            print("-",end=" ")
        else:
            print(stack[-1],end=" ")
        stack.append(arr[i])
    print()
arr = [30, 50, 20, 15, 25]
prevgreater(arr,len(arr))