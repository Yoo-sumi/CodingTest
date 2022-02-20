stack=[]
def balanced_index(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        elif p[i]==')':
            count-=1
        if count==0:
            return i
    return i
def right(p):
    for i in range(len(p)):
        if p[i]=='(':
            stack.append(p[i])
        elif p[i]==')':
            if len(stack)==0:
                return False
            if stack[len(stack)-1]=='(':
                stack.pop()
            else:
                stack.append(p[i])
    if len(stack)==0:
        return True
    else:
        return False
def reverse(p):
    s=""
    for i in range(len(p)):
        if p[i]==')':
            s+='('
        else:
            s+=')'
    return s
answer=""
def solution(p):
    if p=="":
        return ""

    index=balanced_index(p)
    u=p[:index+1]
    v=p[index+1:]

    if right(u):
        answer=u+solution(v)

    elif not right(u):
        s='('
        s+=solution(v)
        s+=')'
        u=u[1:-1]
        s+=reverse(u)
        answer=s

    return answer