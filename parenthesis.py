from collections import deque
def checkpair(val1,val2):
    return (val1=='(' and ')')or (val1=='[' and val2 == ']') or (val1=='{' and val2=='}')
def check_balanced(expr):
    stack=deque()
    for i in range(len(expr)):
        if expr[i]=='(' or expr[i] == '[' or expr[i]=='{':
            stack.append(expr[i])
        else:
            # eg. exp = {{}}}{}
            # if you look closely above {{}} will be matched with pair, Thus, stack "Empty"
            # but an extra closing parenthesis like } will never be matched
            # so there is no point looking forward
            if len(stack)==0:
                return False
            elif checkpair(stack[-1],expr[i]):
                stack.pop()
                continue
            return False
    return True
expr="{{}}}{}"
if check_balanced(expr):
    print("Balanced")
else:
    print("Unbalanced")