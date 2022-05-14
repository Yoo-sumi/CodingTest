n,m=map(int,input().split())
result=[]
array=[]
for i in range(n+1):
    array.append(i)

def is_parent(v):
    if array[v]!=v:
        array[v]=is_parent(array[v])
    return array[v]
def add_team(a,b):
    a=is_parent(a)
    b=is_parent(b)
    if a<b:
        array[b]=a
    else:
        array[a]=b
#[0, 1, 2, 1, 2, 5, 1, 6]
def judge_team(a,b):
    if is_parent(a)==is_parent(b):
        return "YES"
    return "NO"

for _ in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        add_team(b,c)
    elif a==1:
        result.append(judge_team(b,c))
    print(array)
for i in result:
    print(i)