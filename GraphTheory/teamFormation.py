def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return parent[x]

def union(parent,b,c):
    e=find_parent(parent,b)
    f=find_parent(parent,c)
    if e<f:
        parent[f]=e
    else:
        parent[e]=f

n, m=map(int, input().split())

parent=[0]*(n+1)
for i in range(n):
    parent[i]=i


result=[]
for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        union(parent,b,c)
    else:
        if find_parent(parent,b)==find_parent(parent,c):
            result.append("YES")
        else:
            result.append("NO")
    print(parent)
for i in result:
    print(i)
