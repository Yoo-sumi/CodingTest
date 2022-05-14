n,m=map(int,input().split())
parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i
def find_parent(x):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
result=[]
for _ in range(m):
    n,a,b=map(int,input().split())
    if n==0:
        union_parent(a,b)
    elif n==1:
        if find_parent(a)==find_parent(b):
            result.append("YES")
        else:
            result.append("NO")
    print(parent)
for i in result:
    print(i)
