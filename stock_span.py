
# def stockspan(arr):
#     for i in range(len(arr)):
#         curr_span=1
#         j=i-1
#         while j>=0 and arr[j]<=arr[i]:
#             curr_span+=1
#             j=j-1
#         print(curr_span,end=" ")
#     print()
# arr=[12,14,15,7,15,17,5]
# stockspan(arr)

from collections import deque
def stockspan(arr):
    stack=deque()
    stack.append(0)
    print(1,end=" ")
    for i in range(1,len(arr)):
        while len(stack)!=0 and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            print(i+1,end=" ")
        else:
            print(i-stack[-1],end=" ")
        stack.append(i)
    print()
arr=[100, 20, 30, 60, 38, 36, 32, 55, 80, 50, 120]
stockspan(arr)