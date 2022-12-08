def checkalpha(c):
    return c.isalpha()
def precedence(ch,stack_top):
    prec={'+':1,'-':1,'*':2,'/':2,'^':3}
    try:
        a=prec[ch]
        b=prec[stack_top]
        if a<=b:
            return True
        else:
            return False
    except KeyError:
        return False
def convertinfixtopostfix(expr):
    stack=[]
    result=[]
    for i in range(len(expr)):
        if checkalpha(expr[i]):
            result.append(expr[i])
        elif expr[i]=='(':
            stack.append(expr[i])
        elif expr[i]==')':
            while len(stack)>0 and stack[-1]!='(':
                result.append(stack.pop())
            if len(stack)>0 and stack[-1]!='(':
                return 
            else:
                stack.pop()
        else:
            while len(stack) > 0 and precedence(expr[i], stack[-1]):
                result.append(stack.pop())
            stack.append(expr[i])
    while len(stack)>0:
        result.append(stack.pop())
    print("".join(x for x in result))
expresion="a+b*(c^d-e)^(f+g*h)-i"
convertinfixtopostfix(expresion)
