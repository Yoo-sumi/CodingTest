#p="()))((()"
p="(()())()"
stack=[]
def balanced_index(s):
    count=0
    for i in range(len(s)):
        if s[i]=='(':
            count+=1
        if s[i]==')':
            count-=1
        if count==0:
            return i
    return -1
def collect(s):
    count=0
    for i in range(len(s)):
        if count==0 and s[i]==')':
            return False
        if count>0 and s[i]==')':
            count-=1
        elif s[i]=='(':
            count+=1
    if count==0:
        return True
    else:
        return False
def rever(s):
    a=""
    for i in range(len(s)):
        if s[i]=='(':
            a+=')'
        elif s[i]==')':
            a+='('
    return a

def solution(p):
    if p=="":
        return ""
    index=balanced_index(p)
    if index!=-1:
        u=p[:index+1]
        v=p[index+1:]
        if collect(u):
            u+=solution(v)
            return u
        else:
            w="("
            w+=solution(v)
            w+=")"
            w+=rever(u[1:index])
            return w

print(solution(p))