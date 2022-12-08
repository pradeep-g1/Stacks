#stack implementation using collections module

# from collections import deque
# stack=deque()
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)
# top=stack[-1]
# print(top)
# size=len(stack)
# print(size)
# print(str(stack.pop())+" popped")
# print(str(stack.pop())+" popped")
# print(str(stack.pop())+" popped")
# print(str(stack.pop())+" popped")

# This is used to return -infinite whenever our stack is empty
from sys import maxsize
class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return len(self.stack)==0
    # Just use append to add item
    def push(self,item):
        self.stack.append(item)
        print(item+" pushed to stack")
    # Pop removes the top most / last element in stack/list
    def pop(self):
        if self.isEmpty():
            return str(-maxsize-1) #return -infinte
        return self.stack.pop() 
    # Get the topmost element in the stack
    def peek(self):
        if self.isEmpty():
            return str(-maxsize-1)
        return self.stack[len(self.stack)-1]
    def size(self):
        return len(self.stack)
    def dispaly(self):
        print(" ".join(i for i in self.stack[::-1]))
s=Stack()
s.push(str(1))
s.push(str(2))
s.push(str(3))
s.push(str(4))
s.push(str(5))
print(s.pop()+" popped from the stack")
print(s.peek()+" top of the stack")
print(str(s.size())+" size of the stack")
s.dispaly()    

    